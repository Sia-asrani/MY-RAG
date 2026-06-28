def recall_at_k(
    retrieved,
    expected,
    k
):

    retrieved = set(
        retrieved[:k]
    )

    expected = set(
        expected
    )

    return len(
        retrieved & expected
    ) > 0


def reciprocal_rank(
    retrieved,
    expected
):

    for i, chunk in enumerate(retrieved):

        if chunk in expected:

            return 1 / (i + 1)

    return 0