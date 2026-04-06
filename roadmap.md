# AI Organiser: The Lossless Tagger Roadmap 📸

This roadmap focuses on automatically tagging your photography collection with AI and injecting those tags directly into the image's metadata (IPTC/XMP) without altering a single pixel of the image itself.

---

## 🏗️ Phase 1: Foundation & Tools
- [ ] **Environment Setup**: Initialize Python with AI vision (`CLIP`, `Transformers`) and metadata writer (`pyexiftool` or `piexif`).
- [ ] **Core Architecture**: Define the "Analyze then Inject" workflow.

## 🧠 Phase 2: AI Vision Engine
- [ ] **Scene & Object Detection**: Integrate **OpenAI's CLIP** to identify complex scenes (e.g., "Misty mountain at sunrise").
- [ ] **Confidence Filtering**: Logic to only suggest tags with high AI confidence to avoid "wrong" labels.
- [ ] **Technical Analysis**: Extract camera bodies, lenses, and settings (ISO, Aperture) to auto-tag technical shot details.

## 💉 Phase 3: Lossless Metadata Injection
- [ ] **IPTC/XMP Integration**: Develop the module to write AI tags into the standard `Keywords` field.
- [ ] **Pixel Data Integrity**: Implement a "Safety First" check (hashing) to guarantee image data is NEVER modified or re-compressed.
- [ ] **Batch Processing**: Speed-optimised engine to process thousands of images efficiently.

## 🖼️ Phase 4: Photographer Review Gallery (UI)
- [ ] **Sleek UI Design**: A minimalist, dark-themed dashboard to view photos and their AI-suggested tags.
- [ ] **Bulk Approval**: One-click "Commit Tags" button to write thousands of tags at once.
- [ ] **Manual Tweak**: Allow you to quickly add/remove tags before committing.

## 🔎 Phase 5: Search & Sort
- [ ] **Smart Explorer**: Search through your entire library via metadata (even on Windows/macOS file explorers).
- [ ] **Auto-Sorting**: Folder organization based on the newly injected AI tags.

---

> [!IMPORTANT]
> **Photographer's Promise**: This tool handles your photos with the highest care. We use industry-standard metadata protocols (XMP/IPTC) so your shots remain 100% professional and untouched in quality.
