from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance
)

client = QdrantClient(
    path="./qdrant_data"
)

collection_name = "muj_handbook"

if not client.collection_exists(
    collection_name
):

    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    print("Collection created.")

else:

    print("Collection already exists.")

client.close()