def build_context(reranked_results, top_k=3):

    context_parts = []

    for score, chunk in reranked_results[:top_k]:

        context_parts.append(
            f"""
SECTION: {chunk['section']}
SUBSECTION: {chunk['subsection']}
CONTENT:
{chunk['text']}
"""
        )

    return "\n\n".join(context_parts)