def build_context(reranked_results, top_k=3):

    context_parts = []

    for score, chunk in reranked_results[:top_k]:

        context_parts.append(
            f"""
            SECTION: {chunk['section']}
            SUBSECTION: {chunk['subsection']}
            SUBSECTION ID: {chunk['subsection_id']}
            
            CONTENT:
            {chunk['text']}
            """)

    context = "\n\n".join(context_parts)

    return context[:4000]