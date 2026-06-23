from embeddings.retrieval import retrieve
from reranking.reranker import rerank
from rag.context_builder import build_context

query = [
    "What attendance is required?",
    "Can NRI students apply?",
    "What is the code for Architecture?",
    "How is GPA calculated?",
    "What happens if attendance is below 75%?"
]

for q in query:
    print("\n" + "=" * 100)
    print("QUERY:", q)
    print("=" * 100)
    
    retrieved = retrieve(q, top_k=10)

    reranked = rerank(q, retrieved)

    context = build_context(reranked, top_k=3)

    print(context)
    print("\n")