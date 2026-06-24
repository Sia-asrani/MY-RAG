def should_reject(reranked):

    if not reranked:
        return True

    best_score = reranked[0][0]

    if len(reranked) < 2:
        return best_score < -5

    second_score = reranked[1][0]

    gap = best_score - second_score

    print("\nBest:", round(best_score, 4))
    print("Second:", round(second_score, 4))
    print("Gap:", round(gap, 4))

    # very weak relevance

    if best_score < -8:
        return True

    # ambiguous

    if gap < 0.5:
        return True

    return False