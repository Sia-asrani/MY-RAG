import json

from vector_db.search_qdrant import retrieve_qdrant
from reranking.reranker import rerank


def calculate_rank(results, expected_chunks):

    retrieved_ids = [
        chunk["subsection_id"]
        for score, chunk in results
    ]

    best_rank = None

    for chunk_id in expected_chunks:

        if chunk_id in retrieved_ids:

            rank = retrieved_ids.index(chunk_id) + 1

            if best_rank is None:

                best_rank = rank

            else:

                best_rank = min(
                    best_rank,
                    rank
                )

    return best_rank


with open(
    "evaluation/questions.json",
    "r",
    encoding="utf-8"
) as f:

    questions = json.load(f)


retriever_mrr = 0
reranker_mrr = 0

total = len(questions)

print("=" * 100)
print("RERANKER EVALUATION")
print("=" * 100)

for item in questions:

    query = item["question"]

    expected_chunks = item["expected_chunks"]

    # ----------------------------------
    # RETRIEVER
    # ----------------------------------

    retrieved = retrieve_qdrant(
        query,
        top_k=10
    )

    retriever_rank = calculate_rank(
        retrieved,
        expected_chunks
    )

    retriever_rr = (
        1 / retriever_rank
        if retriever_rank
        else 0
    )

    retriever_mrr += retriever_rr

    # ----------------------------------
    # RERANKER
    # ----------------------------------

    reranked = rerank(
        query,
        retrieved
    )

    reranker_rank = calculate_rank(
        reranked,
        expected_chunks
    )

    reranker_rr = (
        1 / reranker_rank
        if reranker_rank
        else 0
    )

    reranker_mrr += reranker_rr

    print("\n" + "-" * 80)

    print("QUESTION:")
    print(query)

    print("\nEXPECTED:")
    print(expected_chunks)

    print(
        f"\nRetriever Rank: {retriever_rank}"
    )

    print(
        f"Retriever RR: {retriever_rr:.4f}"
    )

    print(
        f"Reranker Rank: {reranker_rank}"
    )

    print(
        f"Reranker RR: {reranker_rr:.4f}"
    )


retriever_mrr /= total
reranker_mrr /= total

print("\n" + "=" * 100)

print(
    f"Retriever MRR: {retriever_mrr:.4f}"
)

print(
    f"Reranker MRR: {reranker_mrr:.4f}"
)

print("=" * 100)