from parser.pdf_parser import extract_pages
from parser.chunker import build_chunks
from parser.exporter import export_chunks


pages = extract_pages("data/muj_handbook.pdf")

chunks = build_chunks(pages)

print("\n")
print("=" * 80)

print(f"TOTAL CHUNKS: {len(chunks)}")

print("=" * 80)

for chunk in chunks[:10]:

    print()

    print("-" * 80)

    print("ID:", chunk.id)

    print("PAGE:", chunk.page)

    print("SECTION:", chunk.section)

    print("SUBSECTION:", chunk.subsection)

    print("SUBSECTION ID:", chunk.subsection_id)

    print()

    print(chunk.text[:500])

    print()

export_chunks(
    chunks,
    "output/chunks.json"
)

print("\nchunks.json exported")