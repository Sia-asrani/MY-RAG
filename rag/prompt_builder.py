def build_prompt(query, context):

    return f"""
You are an assistant that answers questions
using ONLY the provided handbook context.

Rules:

1. Use only the context.
2. If the answer is not present, say:
   "I could not find that information in the handbook."
3. Be concise.
4. Cite the subsection when possible.

CONTEXT:

{context}

QUESTION:

{query}

ANSWER:
"""