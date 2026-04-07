from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
import os
import numpy as np

try:
    import rawpy
except ImportError:
    rawpy = None

class VisionEngine:
    """
    AI Vision Engine using OpenAI's CLIP model for zero-shot image tagging.
    Enhanced with rawpy for professional RAW image analysis (.ARW, .CR2, .NEF, etc.).
    """
    
    def __init__(self, model_id="openai/clip-vit-large-patch14"):
        print(f"🔄 Initializing Pro-Grade CLIP model ({model_id})...")
        self.model = CLIPModel.from_pretrained(model_id)
        self.processor = CLIPProcessor.from_pretrained(model_id)
        
        # Acceleration detection: NVIDIA CUDA > Windows DirectML (NPU) > CPU
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            try:
                import torch_directml
                self.device = torch_directml.device()
                print("⚡ NPU Acceleration enabled via DirectML!")
            except:
                self.device = "cpu"
                print("⚠️ No NPU/GPU detected. Falling back to CPU (Slow).")
                
        self.model.to(self.device)
        print(f"✅ AI Engine ready on {self.device}")

    def load_image(self, image_path):
        """Loads an image with special handling for RAW files."""
        ext = os.path.splitext(image_path)[1].lower()
        
        # If it's a RAW file and rawpy is available, develop a preview
        if ext in ['.arw', '.cr2', '.nef', '.dng', '.orf'] and rawpy:
            try:
                with rawpy.imread(image_path) as raw:
                    # Develop a fast, low-resolution thumbnail for CLIP analysis
                    rgb = raw.postprocess(use_camera_wb=True, half_size=True, no_auto_bright=True, bright=1.0)
                    return Image.fromarray(rgb)
            except Exception as e:
                print(f"⚠️ rawpy failed on {os.path.basename(image_path)}, falling back to pillow: {e}")
        
        # Default back to Pillow for standard formats (or if rawpy fails)
        return Image.open(image_path)

    def analyze_image(self, image_path, candidate_labels, confidence_threshold=0.3):
        """Analyzes the image and returns tags that pass the confidence threshold."""
        try:
            image = self.load_image(image_path)
            
            inputs = self.processor(text=candidate_labels, images=image, return_tensors="pt", padding=True)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            with torch.no_grad():
                outputs = self.model(**inputs)
            
            logits_per_image = outputs.logits_per_image
            probs = logits_per_image.softmax(dim=1)
            
            results = []
            for i, label in enumerate(candidate_labels):
                confidence = float(probs[0][i])
                if confidence >= confidence_threshold:
                    results.append({"label": label, "confidence": round(confidence, 4)})
            
            return sorted(results, key=lambda x: x["confidence"], reverse=True)
            
        except Exception as e:
            print(f"❌ Error analyzing {os.path.basename(image_path)}: {str(e)}")
            return []

if __name__ == "__main__":
    PHOTO_LABELS = ["landscape", "portrait", "street", "macro", "nature", "urban"]
    data_dir = "data/"
    files = [f for f in os.listdir(data_dir) if f.lower().endswith(".arw")]
    if files:
        test_file = os.path.join(data_dir, files[0])
        engine = VisionEngine()
        tags = engine.analyze_image(test_file, PHOTO_LABELS)
        print(f"Tags: {tags}")
