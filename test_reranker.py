from embeddings.retrieval import retrieve
from reranking.reranker import rerank


query = "What attendance is required?"


retrieved = retrieve(
    query,
    top_k=10
)

reranked = rerank(
    query,
    retrieved
)

print("\nRERANKED RESULTS\n")

for score, chunk in reranked[:5]:

    print("=" * 80)

    print("Score:", round(score, 4))

    print("Chunk:", chunk["subsection_id"])

    print("Subsection:", chunk["subsection"])

    print()

    print(chunk["text"][:300])

    print()