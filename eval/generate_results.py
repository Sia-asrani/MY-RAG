import json

from embeddings.retrieval import retrieve

with open(
    "eval/questions.json",
    "r",
    encoding="utf-8"
) as f:

    questions = json.load(f)

results_json = []

for item in questions:

    query = item["question"]

    results = retrieve(
        query,
        top_k=5
    )

    retrieved = []

    for rank, r in enumerate(results, start=1):

        retrieved.append({

            "rank": rank,

            "chunk_id": r.payload["id"],

            "score": round(
                float(r.score),
                4
            ),

            "page": r.payload["page"],

            "section": r.payload["section"],

            "text": r.payload["text"]

        })

    results_json.append({

        "question": query,

        "results": retrieved

    })

with open(
    "eval/retrieval_results.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        results_json,
        f,
        indent=4,
        ensure_ascii=False
    )

print("retrieval_results.json created.")