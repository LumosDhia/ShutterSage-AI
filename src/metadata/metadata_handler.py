import os
import hashlib

class MetadataHandler:
    """
    Handles metadata for photography files using XMP Sidecar files.
    This ensures 100% pixel-perfect integrity of the original RAW files
    while allowing professional software (Lightroom, Capture One) to read the tags.
    """
    
    @staticmethod
    def get_file_hash(file_path):
        """Generates a SHA-256 hash of the file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Image not found at {file_path}")
        self.sidecar_path = f"{os.path.splitext(file_path)[0]}.xmp"

    def add_tags(self, tags: list):
        """
        Generates or updates an XMP sidecar file with the provided tags.
        """
        try:
            # Create the keyword XML block
            keyword_items = "".join([f"     <rdf:li>{tag}</rdf:li>\n" for tag in tags])
            
            # Simple but valid XMP Template
            xmp_content = f"""<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='AI-Picture-Tager'>
 <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
  <rdf:Description rdf:about=''
    xmlns:dc='http://purl.org/dc/elements/1.1/'
    xmlns:xmp='http://ns.adobe.com/xap/1.0/'>
   <dc:subject>
    <rdf:Bag>
{keyword_items}    </rdf:Bag>
   </dc:subject>
   <xmp:CreatorTool>AI-Picture-Tager</xmp:CreatorTool>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>"""

            with open(self.sidecar_path, 'w', encoding='utf-8') as f:
                f.write(xmp_content)
                
            print(f"✅ Created XMP sidecar: {os.path.basename(self.sidecar_path)} with {len(tags)} tags")
            return True
        except Exception as e:
            print(f"❌ Error creating sidecar: {str(e)}")
            return False

    def verify_integrity(self, expected_hash: str):
        """
        Original file should never change when using sidecars.
        Returns (is_valid, current_hash).
        """
        current_hash = self.get_file_hash(self.file_path)
        return current_hash == expected_hash, current_hash

if __name__ == "__main__":
    # Test on one of the copied images
    test_file = "data/DSC02522.ARW"
    if os.path.exists(test_file):
        handler = MetadataHandler(test_file)
        handler.add_tags(["ai-landscape", "mountains", "nature"])
    else:
        print("Test file not found.")
