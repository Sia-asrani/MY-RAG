import json

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


for i in range(len(questions)):

    print("\n")
    print("=" * 100)

    print(
        questions[i]["question"]
    )

    print("=" * 100)

    for chunk in retrieved[i]["results"]:

        print()

        print(
            f"Rank {chunk['rank']}"
        )

        print(
            "Chunk:",
            chunk["chunk_id"]
        )

        print(
            "Score:",
            chunk["score"]
        )

        print(
            "Page:",
            chunk["page"]
        )

        print(
            "Section:",
            chunk["section"]
        )

        print()

        print(
            chunk["text"][:300]
        )

        print()

    ids = input(

        "\nRelevant chunk ids (comma separated): "

    )

    questions[i]["expected_ids"] = [

        x.strip()

        for x in ids.split(",")

        if x.strip()

    ]


with open(
    "eval/questions.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        questions,
        f,
        indent=4,
        ensure_ascii=False
    )

print()

print("questions.json updated.")