from sentence_transformers import SentenceTransformer

#change to "BAAI/bge-small-en-v1.5", if problem
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    device="cpu"
)


def embed_text(text):

    return model.encode(
        text,
        normalize_embeddings=True
    )
    
    
    