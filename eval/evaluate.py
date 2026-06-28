import json

from eval.metrics import (
    recall_at_k,
    reciprocal_rank
)

with open(
    "eval/questions.json",
    "r",
    encoding="utf-8"
) as f:

    questions = json.load(f)

with open(
    "eval/retrieval_results.json",
    "r",
    encoding="utf-8"
) as f:

    retrieved = json.load(f)

r1 = 0
r3 = 0
r5 = 0
mrr = 0

total = len(questions)

for q, result in zip(
    questions,
    retrieved
):

    retrieved_ids = [

        r["chunk_id"]

        for r in result["results"]

    ]

    expected = q["expected_ids"]

    if recall_at_k(
        retrieved_ids,
        expected,
        1
    ):
        r1 += 1

    if recall_at_k(
        retrieved_ids,
        expected,
        3
    ):
        r3 += 1

    if recall_at_k(
        retrieved_ids,
        expected,
        5
    ):
        r5 += 1

    mrr += reciprocal_rank(
        retrieved_ids,
        expected
    )

print()

print("=" * 60)

print("Retriever Evaluation")

print("=" * 60)

print(
    f"Recall@1 : {r1/total:.2%}"
)

print(
    f"Recall@3 : {r3/total:.2%}"
)

print(
    f"Recall@5 : {r5/total:.2%}"
)

print(
    f"MRR       : {mrr/total:.4f}"
)

print("=" * 60)