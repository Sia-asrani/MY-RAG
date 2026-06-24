import json

from vector_db.search_qdrant import retrieve_qdrant


with open(
    "evaluation/questions.json",
    "r",
    encoding="utf-8"
) as f:

    questions = json.load(f)


correct = 0
total = len(questions)

mrr_total = 0

for item in questions:

    query = item["question"]

    expected = item["expected_chunk"]

    retrieved = retrieve_qdrant(
        query,
        top_k=5
    )

    retrieved_ids = [
        chunk["subsection_id"]
        for score, chunk in retrieved
    ]

    found = expected in retrieved_ids
    if found:
        correct += 1
        rank = (
            retrieved_ids.index(expected)
            + 1)
        reciprocal_rank = 1 / rank
        mrr_total += reciprocal_rank
    else:
        reciprocal_rank = 0

    print("\n", query)
    print("Expected:", expected)
    print("Retrieved:", retrieved_ids)
    print("Found:", found)
    
    mrr = mrr_total / total
    print(
        f"\nMRR: {mrr:.4f}"
    )


print("\n" + "=" * 50)

print(
    f"Recall@5: {correct/total:.2%}"
)