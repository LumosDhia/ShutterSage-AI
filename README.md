# AI-Picture-Tager

AI-powered CLI for zero-shot image metadata tagging with NPU acceleration.

## Technical Specifications
- **Vision Model**: CLIP Large (openai/clip-vit-large-patch14)
- **Hardare Acceleration**: NPU/GPU via DirectML (Windows)
- **Media Support**: RAW (.ARW, .CR2, .NEF) and standard formats (.JPG, .PNG)
- **Metadata Output**: Standard dc:subject XMP sidecars

## Usage
Activate virtual environment and run main.py specifying a directory or file.

```powershell
python main.py "C:\Path\To\Imagery" --threshold 0.05
```

## Quick Start
Run the automation wizard:
```powershell
.\start.ps1
```
