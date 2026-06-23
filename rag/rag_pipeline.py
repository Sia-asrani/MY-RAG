from vector_db.search_qdrant import retrieve_qdrant
from reranking.reranker import rerank
from rag.context_builder import build_context
from rag.prompt_builder import build_prompt
from rag.llm_client import generate_answer

sim_thresh = 0.35

def ask_handbook(query):
    
    print("\n" + "=" * 80)
    print("QUERY:", query)
    print("=" * 80)
    
    retrieved = retrieve_qdrant(
    query,
    top_k=10)
    
    if not retrieved:
        return "I could not find that information in the handbook."

    best_score = retrieved[0][0]

    print(f"\nBest Retrieval Score: {best_score:.4f}")

    print("\nTop Retrieved Results:")

    for score, chunk in retrieved[:5]:

        print(
            f"{chunk['subsection_id']} | "
            f"{round(score, 4)} | "
            f"{chunk['subsection']}"
        )

    filtered = []

    for score, chunk in retrieved:

        if score >= sim_thresh:

            filtered.append(
                (
                    score,
                    chunk
                )
            )

    print(
        f"\nChunks after threshold ({sim_thresh}): "
        f"{len(filtered)}"
    )

    if len(filtered) == 0:

        return (
            "I could not find that information "
            "in the handbook."
        )
    reranked = rerank(
            query,
            filtered
        )

    print("\nTop Reranked Results:")

    for score, chunk in reranked[:5]:

        print(
                f"{chunk['subsection_id']} | "
                f"{round(score, 4)} | "
                f"{chunk['subsection']}"
            )
        
    context = build_context(
        reranked,
        top_k=3
    )

    print("\nContext Length:")
    print(len(context))

    print("\nContext Preview:")
    print(context[:500])

    prompt = build_prompt(
        query,
        context
    )

    print("\nPrompt Length:")
    print(len(prompt))

    answer = generate_answer(prompt)

    return answer


if __name__ == "__main__":

    while True:

        query = input(
            "\nAsk a question (q to quit): "
        )

        if query.lower() == "q":
            break

        answer = ask_handbook(
            query
        )

        print("\nANSWER:\n")

        print(answer)