#what does the extraction look like 

from parser.pdf_parser import extract_pages

pages = extract_pages("data/muj_handbook.pdf")

print(f"Pages: {len(pages)}")

for page in pages[:5]:
    print("=" * 50)
    print(f"PAGE {page['page']}")
    print(page["text"][:1000])