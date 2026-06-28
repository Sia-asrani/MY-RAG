from qdrant_client import QdrantClient

from embeddings.embedder import embed_text


client = QdrantClient(
    path="./qdrant_db"
)

COLLECTION_NAME = "muj_handbook"


def retrieve(query, top_k=5):

    query_embedding = embed_text(
        query
    ).tolist()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=top_k
    )

    return results.points


results = retrieve(
    "What attendance is required?"
)

for r in results:

    print("=" * 80)
    print("Score:", round(r.score, 4))
    print("Section:", r.payload["section"])
    print()
    print(r.payload["text"][:300])
    
#client.close()