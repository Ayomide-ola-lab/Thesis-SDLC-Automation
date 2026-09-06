import os
import sys
import base64
from pathlib import Path
import openai
from dotenv import load_dotenv

import fitz  # PyMuPDF

# Setup paths and environment
CURRENT_DIR = Path(__file__).parent
AUTODOC_ROOT = CURRENT_DIR.parent
load_dotenv(AUTODOC_ROOT / ".env")

client = openai.OpenAI()
pdf_path = CURRENT_DIR / "Architecture diagram" / "OptArrow_Architecture.pdf"

def pdf_to_base64_image(pdf_path: Path) -> str:
    """Converts the first page of a PDF into a base64 encoded PNG image."""
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    # Use a higher DPI for clear text reading by the Vision model
    pix = page.get_pixmap(dpi=200)
    img_bytes = pix.tobytes("png")
    return base64.b64encode(img_bytes).decode('utf-8')

def extract_architecture_from_vision(base64_img: str) -> str:
    """Sends the image to GPT-4o Vision API to extract authoritative architecture knowledge."""
    prompt = """You are an Expert Systems Architect. Analyze this high-level architecture diagram of the OptArrow optimization integration engine.
    
    Extract a comprehensive, highly technical engineering breakdown containing:
    1. System Boundaries & External Actors (Who/what interacts with the system)
    2. Core Components (e.g., Gateways, Engines, Solvers, specific technologies shown)
    3. Data Flows & Protocols (e.g., HTTP, Arrow IPC, arrows denoting flow directions)
    
    This output will be injected into our Automated SDLC Pipeline as 'AUTHORITATIVE SYSTEM KNOWLEDGE'. 
    Be highly precise, do not invent components that are not in the diagram, and format your output in clean Markdown."""
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_img}"}}
                ]
            }
        ],
        max_tokens=2000,
        temperature=0.1
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(f"Reading Architecture Diagram from: {pdf_path}")
    if not pdf_path.exists():
        print("ERROR: PDF diagram not found at specified path!")
        sys.exit(1)
        
    print("Converting PDF to high-resolution PNG for Vision processing...")
    b64_img = pdf_to_base64_image(pdf_path)
    
    print("Sending diagram to GPT-4o Vision API for architectural synthesis...")
    extracted_text = extract_architecture_from_vision(b64_img)
    
    output_dir = CURRENT_DIR / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "Experimental_Vision_Architecture.md"
    output_file.write_text(extracted_text, encoding="utf-8")
    
    print("\n===========================================")
    print(" VISION EXTRACTION SUCCESSFUL ")
    print("===========================================\n")
    print(extracted_text[:500] + "\n\n... (truncated for console output)")
    print(f"\nFull extraction saved to: {output_file}")
