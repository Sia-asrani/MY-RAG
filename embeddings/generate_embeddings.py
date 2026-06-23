import json

from embedder import embed_text

with open(
    "output/chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)

for chunk in chunks:
    combined_text = f"""
    Section: {chunk['section']}
    Subsection: {chunk['subsection']}
    Content: {chunk['text']}
    """

    chunk["embedding"] = embed_text(combined_text).tolist()


with open(
    "output/chunks_with_embeddings.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        chunks,
        f,
        indent=2
    )

print("Embeddings generated.")