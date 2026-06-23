from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

def rerank(query, retrieved_chunks):

    pairs = []

    for score, chunk in retrieved_chunks:

        pairs.append(
            (
                query,
                chunk["text"]
            )
        )

    rerank_scores = model.predict(
        pairs
    )

    results = []

    for score, (_, chunk) in zip(
        rerank_scores,
        retrieved_chunks
    ):
        results.append(
            (
                float(score),
                chunk
            )
        )

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return results