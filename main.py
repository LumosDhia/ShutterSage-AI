import argparse
import os
import sys
from rich.console import Console
from rich.theme import Theme
from src.core.processor import ShutterSageProcessor

# --- Catppuccin Macchiato Theme ---
macchiato_theme = Theme({
    "info": "#8aadf4",      # Blue
    "success": "#a6da95",   # Green
    "warning": "#eed49f",   # Yellow
    "error": "#ed8796",     # Red
    "highlight": "#c6a0f6", # Mauve
})
console = Console(theme=macchiato_theme)

def main():
    parser = argparse.ArgumentParser(description="ShutterSage-AI: The Lossless AI Photo Tagger")
    parser.add_argument("path", help="The directory or specific file to process (.ARW, .JPG, .PNG)")
    parser.add_argument("--threshold", type=float, default=0.25, help="Confidence threshold for AI tags (default: 0.25)")
    parser.add_argument("--recursive", action="store_true", help="Process subdirectories recursively")
    
    args = parser.parse_args()

    processor = ShutterSageProcessor(confidence_threshold=args.threshold)

    # Handle single file or directory
    target = args.path
    if not os.path.exists(target):
        console.print(f"[error]Error: {target} does not exist.[/error]")
        sys.exit(1)

    console.print("--- ShutterSage-AI: [highlight]Initializing Analysis Engine[/highlight] ---", style="info")
    
    if os.path.isfile(target):
        # Process single file
        processor.process_single_file(target)
    elif os.path.isdir(target):
        # Process directory
        if args.recursive:
            for root, _, files in os.walk(target):
                if any(f.lower().endswith(('.arw', '.jpg', '.jpeg', '.png')) for f in files):
                    processor.process_directory(root)
        else:
            processor.process_directory(target)

    console.print("--- [success]Analysis Complete[/success]: All metadata tags committed via XMP ---", style="highlight")

if __name__ == "__main__":
    main()
