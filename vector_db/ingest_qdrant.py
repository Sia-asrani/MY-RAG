import json

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct


client = QdrantClient(
    path="./qdrant_data"
)

with open(
    "output/chunks_with_embeddings.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)


points = []

for idx, chunk in enumerate(chunks):

    point = PointStruct(
        id=idx,

        vector=chunk["embedding"],

        payload={
            "chunk_id": chunk["id"],
            "section": chunk["section"],
            "subsection": chunk["subsection"],
            "subsection_id": chunk["subsection_id"],
            "text": chunk["text"]
        }
    )

    points.append(point)


client.upsert(
    collection_name="muj_handbook",
    points=points
)

print(
    f"Inserted {len(points)} points."
)

client.close()