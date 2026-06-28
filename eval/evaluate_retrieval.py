from embeddings.retrieval import retrieve

from eval.utils import (
    load_questions
)


questions = load_questions(
    "eval/questions.json"
)


for item in questions:

    print("\n")
    print("=" * 100)

    print(item["question"])

    print("=" * 100)

    results = retrieve(
        item["question"],
        top_k=5
    )

    for i, r in enumerate(results):

        print()

        print(
            f"Rank {i+1}"
        )

        print(
            "Chunk:",
            r.payload["id"]
        )

        print(
            "Score:",
            round(r.score,4)
        )

        print(
            "Chunk:",
            r.payload["id"]
        )

        print(
            "Page:",
            r.payload["page"]
        )

        print(
            "Section:",
            r.payload["section"]
        )

        print()

        print(
            r.payload["text"][:250]
        )