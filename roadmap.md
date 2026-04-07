# AI-Picture-Tager: The Lossless Tagger Roadmap 📸

This roadmap focuses on a high-performance CLI tool for automatically tagging your photography collection with AI and injecting those tags directly into the image's metadata (IPTC/XMP) without altering a single pixel of the image itself.

---

## 🏗️ Phase 1: Foundation & Tools
- [x] **Environment Setup**: Initialised Python venv with AI vision (`CLIP`, `Transformers`) and metadata writer (`pyexiv2`).
- [x] **Core Architecture**: Defined the "Analyze then Inject" workflow (`src/core/processor.py`).
- [x] **CLI Removal of Website**: Scrapped the web interface to focus on a robust, lightweight command-line tool.

## 🧠 Phase 2: AI Vision Engine
- [x] **Scene & Object Detection**: Integrating **OpenAI's CLIP** model for zero-shot tagging (`src/ai/vision_engine.py`).
- [x] **Confidence Filtering**: Initial logic implemented and tested.
- [ ] **Technical Analysis**: Extracting technical shot details (ISO, Aperture).
- [ ] **NPU Acceleration**: Optimise for Snapdragon NPU to speed up local analysis.

## 💉 Phase 3: Lossless Metadata Injection
- [x] **XMP Sidecar Integration**: Developed the module to write AI tags into standard `dc:subject`.
- [ ] **Safety First (Hashing)**: Implement a hashing check to guarantee RAW files remain mathematically identical.
- [ ] **Batch Processing**: Speed-optimised engine to process thousands of images efficiently via CLI.

## 🔎 Phase 4: Search & Sort
- [ ] **Manual CLI Tweak**: Commands to quickly review or modify AI-suggested tags before committing.
- [ ] **Smart Explorer**: Search through your entire library via metadata tags.
- [ ] **Auto-Sorting**: Folder organization based on the newly injected AI tags.

## 🚀 Phase 5: Pro Features
- [ ] **Face Recognition**: Local integration for privacy-first person tagging.
- [ ] **Similarity Grouping**: Find similar shots (even if exposure differs) to help with culling.
- [ ] **Lightroom Plugin**: Direct integration to trigger AI tagging from within Adobe Lightroom.

## 📁 Phase 6: Automation & Export
- [ ] **Smart Folder Structure**: Automatically move or copy files into folder hierarchies based on AI tags.
- [ ] **Cloud Sync (Optional)**: Securely backup XMP sidecars to a personal cloud for universal access.
- [ ] **Export for Social**: One-click "Ready for Instagram" export with auto-captioning based on tags.

---

> [!IMPORTANT]
> **Photographer's Promise**: This tool handles your photos with the highest care. We use industry-standard metadata protocols (XMP/IPTC) so your shots remain 100% professional and untouched in quality.
