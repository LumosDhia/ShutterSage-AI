import os
from rich.console import Console
from rich.theme import Theme
from src.ai.vision_engine import VisionEngine
from src.metadata.metadata_handler import MetadataHandler

# Catppuccin Macchiato Theme Definition
macchiato_theme = Theme({
    "info": "#8aadf4",      # Blue
    "success": "#a6da95",   # Green
    "warning": "#eed49f",   # Yellow
    "error": "#ed8796",     # Red
    "highlight": "#c6a0f6", # Mauve
    "text": "#cad3f5"       # Text
})
console = Console(theme=macchiato_theme)

PHOTO_LABELS = [
    # --- Subjects & Scenes ---
    "landscape", "mountain-range", "snowy-peak", "forest-path", "wildlife", "ocean-coastline",
    "scenic-view", "urban-cityscape", "architecture", "street-photography", "candid-moment",
    "travel-photography", "portrait-session", "macro-details", "floral", "minimalist-composition",
    "people", "person", "crowd", "street-life", "animals", "building", "vehicle", "car",
    
    # --- Lighting & Atmosphere ---
    "golden-hour", "blue-hour", "dramatic-lighting", "soft-natural-light", "harsh-sunlight",
    "misty-atmosphere", "foggy-morning", "stormy-clouds", "silhouette", "backlit",
    "long-exposure-water", "night-sky", "star-trails", "bokeh-background", "rim-light",
    "sunny", "cloudy", "overcast", "rainy", "snowy", "winter", "autumn", "spring", "summer",
    
    # --- Style & Aesthetic ---
    "cinematic-look", "moody-atmosphere", "vibrant-colors", "muted-tones", "high-contrast",
    "black-and-white", "grainy-film-aesthetic", "low-key", "high-key", "painterly-texture",
    "industrial-vibe", "vintage-feel", "modern-clean", "dark-and-gritty", "airy-and-light",
    "minimalist", "clean-lines", "symmetry", "leading-lines", "rule-of-thirds",
    
    # --- Emotions & Narrative ---
    "serenity", "adventure", "loneliness", "nostalgia", "mystery", "energy", 
    "calmness", "melancholy", "vastness", "intimacy", "peaceful", "solitude", "wonder"
]

SUPPORTED_EXTENSIONS = ('.arw', '.jpg', '.jpeg', '.png', '.cr2', '.nef', '.dng', '.orf')

class ShutterSageProcessor:
    def __init__(self, confidence_threshold=0.3):
        self.engine = VisionEngine()
        self.confidence_threshold = confidence_threshold

    def process_single_file(self, file_path):
        """Processes a single image file."""
        if not os.path.exists(file_path):
            console.print(f"[error]File {file_path} not found.[/error]")
            return
            
        file_name = os.path.basename(file_path)
        console.print(f"Processing [highlight]{file_name}[/highlight]...", style="info")
        
        # 1. Analyze with AI
        tags = self.engine.analyze_image(file_path, PHOTO_LABELS, self.confidence_threshold)
        tag_list = [t['label'] for t in tags]
        
        if tag_list:
            console.print(f"[success]✅ Found {len(tag_list)} tags:[/success] [highlight]{', '.join(tag_list)}[/highlight]")
            # 2. Inject Metadata
            handler = MetadataHandler(file_path)
            success = handler.add_tags(tag_list)
            return {"file": file_name, "tags": tag_list, "success": success}
        else:
            console.print(f"[warning]⚠️ No high-confidence tags found for {file_name}[/warning]")
            return {"file": file_name, "tags": [], "success": True}

    def process_directory(self, directory_path):
        """Processes all supported images in a directory."""
        if not os.path.isdir(directory_path):
            console.print(f"[error]Directory {directory_path} not found.[/error]")
            return

        files = [f for f in os.listdir(directory_path) if f.lower().endswith(SUPPORTED_EXTENSIONS)]
        console.print(f"🔍 Found [highlight]{len(files)}[/highlight] images to process in {directory_path}...", style="info")

        results = []
        for file_name in files:
            file_path = os.path.join(directory_path, file_name)
            res = self.process_single_file(file_path)
            results.append(res)
        
        return results

if __name__ == "__main__":
    # Test directory
    test_dir = "data/"
    if os.path.exists(test_dir):
        processor = ShutterSageProcessor()
        processor.process_directory(test_dir)
    else:
        console.print("[error]Data directory not found. Create it or fix path.[/error]")
