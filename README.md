# AI-Picture-Tager 📸🧙‍♂️

**A professional AI-powered CLI tool that injects smart tags directly into your image metadata with 100% pixel-perfect integrity.**

---

## 🌟 Key Features
- **AI Semantic Tagging**: Uses deep learning to high-quality tag objects, scenes, and emotions in your photos.
- **Lossless Metadata Injection**: Writes tags directly into IPTC/XMP `Keywords` fields without re-compressing or touching your pixels.
- **CLI Mastery**: Lightweight, no browser required. Process thousands of images from your terminal.
- **Universal Compatibility**: Tags are readable by Adobe Lightroom, Bridge, Windows Photos, and macOS Finder.

## 🛠️ Usage
1. **Installation**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Process a Directory**:
   ```bash
   python main.py "C:\Path\To\My\Photos"
   ```
3. **Advanced Options**:
   ```bash
   python main.py "C:\Path\To\My\Photos" --threshold 0.35 --recursive
   ```

## 📦 Requirements
Check [requirements.txt](requirements.txt) for the list of Python dependencies.

## 🗺️ Roadmap
See the [roadmap.md](roadmap.md) for future plans and architectural details.

---
*Created with care by AI-Picture-Tager.*
