import json

from embedder import embed_text
from similarity import cosine_similarity

#load chunks
with open(
    "output/chunks_with_embeddings.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)
    
#retreive chunks
def retrieve(query, top_k=5):

    query_embedding = embed_text(query)

    scores = []

    for chunk in chunks:

        score = cosine_similarity(
            query_embedding,
            chunk["embedding"]
        )

        scores.append(
            (
                score,
                chunk
            )
        )

    scores.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return scores[:top_k]

#test query
results = retrieve(
    "What attendance is required?"
)

#results
print("\nTOP RESULTS\n")

for score, chunk in results:

    print("=" * 80)

    print("Score:", round(score, 4))

    print("Chunk ID:", chunk["id"])

    print("Section:", chunk["section"])

    print("Subsection:", chunk["subsection"])

    print("Subsection ID:", chunk["subsection_id"])

    print()

    print(chunk["text"][:300])

    print()