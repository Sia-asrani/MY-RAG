import json

from qdrant_client import QdrantClient
from qdrant_client.models import (
    PointStruct,
    VectorParams,
    Distance
)

from embeddings.embedder import embed_text


client = QdrantClient(
    path="./qdrant_db"
)

COLLECTION_NAME = "muj_handbook"


collections = client.get_collections()

existing = [
    c.name
    for c in collections.collections
]

if COLLECTION_NAME not in existing:

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )


with open(
    "output/chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)


points = []

for idx, chunk in enumerate(chunks):

    combined_text = f"""
    Major Section: {chunk.get('major_section','')}
    Section: {chunk.get('section','')}
    Subsection: {chunk.get('subsection','')}

    {chunk['text']}
    """

    embedding = embed_text(
        combined_text
    )

    points.append(
        PointStruct(
            id=idx,
            vector=embedding.tolist(),
            payload=chunk
        )
    )

client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print(
    f"Uploaded {len(points)} chunks."
)

#client.close()