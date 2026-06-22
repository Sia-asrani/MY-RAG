#what does the extraction look like 

from parser.pdf_parser import extract_pages


from pathlib import Path

pdf_path = Path("data") / "muj_handbook.pdf"

pages = extract_pages(pdf_path)

print(f"Pages: {len(pages)}")

for page in pages[20:30]:
    print("=" * 50)
    print(f"PAGE {page['page']}")
    print(page["text"][:1000])