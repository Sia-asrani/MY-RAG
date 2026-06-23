def build_prompt(query, context):

    return f"""
You are an academic handbook assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

"I could not find that information in the handbook."

Context:

{context}

Question:

{query}

Answer:
"""