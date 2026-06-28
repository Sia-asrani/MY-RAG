from qdrant_client import QdrantClient

client = QdrantClient(
    path="./qdrant_db"
)

info = client.get_collection(
    "muj_handbook"
)

print(info)

#client.close()