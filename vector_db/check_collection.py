from qdrant_client import QdrantClient

client = QdrantClient(
    path="./qdrant_data"
)

info = client.get_collection(
    "muj_handbook"
)

print(info)

client.close()