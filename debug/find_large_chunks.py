import json

with open(
    "output/chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)

for chunk in chunks:

    words = len(
        chunk["text"].split()
    )

    if words > 1000:

        print("\n" + "="*80)

        print(
            f"ID: {chunk['id']}"
        )

        print(
            f"WORDS: {words}"
        )

        print(
            f"TYPE: {chunk['chunk_type']}"
        )

        print(
            f"SECTION: {chunk['section']}"
        )

        print(
            f"SUBSECTION: {chunk['subsection']}"
        )

        print("\nFIRST 500 CHARS:\n")

        print(
            chunk["text"][:500]
        )

        print("\nLAST 500 CHARS:\n")

        print(
            chunk["text"][-500:]
        )