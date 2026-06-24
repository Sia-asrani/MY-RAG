from vector_db.search_qdrant import retrieve_qdrant
from reranking.reranker import rerank
from rag.context_builder import build_context
from rag.prompt_builder import build_prompt
from rag.llm_client import generate_answer


def should_reject(reranked_results):

    if not reranked_results:
        return True
    best_score = reranked_results[0][0]
    if len(reranked_results) == 1:
        return best_score < 0

    second_score = reranked_results[1][0]

    score_gap = best_score - second_score

    print("\nBest Rerank Score:", round(best_score, 4))
    print("Second Rerank Score:", round(second_score, 4))
    print("Score Gap:", round(score_gap, 4))

    #rejection rule: if everything is similarly bad, we probably don't have a real answer
    if best_score < -5 and score_gap < 1:
        return True

    return False


def ask_handbook(query):

    print("\n" + "=" * 80)
    print("QUERY:", query)
    print("=" * 80)
    retrieved = retrieve_qdrant(query, top_k=10)

    if not retrieved:
        return "I could not find that information in the handbook."

    print("\nTop Retrieved Results:")

    for score, chunk in retrieved[:5]:

        print(
            f"{chunk['subsection_id']} | "
            f"{round(score, 4)} | "
            f"{chunk['subsection']}"
        )

    reranked = rerank(query, retrieved)

    print("\nTop Reranked Results:")

    for score, chunk in reranked[:5]:

        print(
            f"{chunk['subsection_id']} | "
            f"{round(score, 4)} | "
            f"{chunk['subsection']}"
        )

    if should_reject(reranked):

        return (
            "I could not find that information "
            "in the handbook."
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

    answer = generate_answer(
        prompt
    )

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