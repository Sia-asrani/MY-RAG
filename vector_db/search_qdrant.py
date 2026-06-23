from qdrant_client import QdrantClient

from embeddings.embedder import embed_text

client = QdrantClient(
    path="./qdrant_data"
)

def retrieve_qdrant(
    query,
    top_k=10
):

    query_vector = embed_text(
        query
    ).tolist()

    results = client.query_points(
        collection_name="muj_handbook",

        query=query_vector,

        limit=top_k
    )

    retrieved = []

    for point in results.points:

        retrieved.append(
            (
                point.score,
                point.payload
            )
        )

    return retrieved


if __name__ == "__main__":

    query = "What attendance is required?"

    results = retrieve_qdrant(
        query,
        top_k=5
    )

    for score, payload in results:

        print("=" * 80)

        print(
            "Score:",
            round(score, 4)
        )

        print(
            "Chunk:",
            payload["chunk_id"]
        )

        print(
            "Subsection:",
            payload["subsection"]
        )

        print()

        print(
            payload["text"][:300]
        )

        print()
        
        client.close()