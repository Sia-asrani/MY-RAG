import json

with open(
    "output/chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)

lengths = [len(chunk["text"]) for chunk in chunks]

print("Min:", min(lengths))
print("Max:", max(lengths))
print("Avg:", sum(lengths)/len(lengths))

lengths = [len(chunk["text"].split()) for chunk in chunks]

print("Min:", min(lengths))
print("Max:", max(lengths))
print("Avg:", sum(lengths)/len(lengths))

lengths = [len(chunk["text"].split()) for chunk in chunks]

print(f"Chunks: {len(lengths)}")
print(f"Min: {min(lengths)}")
print(f"Max: {max(lengths)}")
print(f"Avg: {sum(lengths)/len(lengths):.2f}")

print("\nTop 10 largest chunks:")
for c in sorted(chunks,
                key=lambda x: len(x["text"].split()),
                reverse=True)[:10]:

    print(
        f"{len(c['text'].split())} words | "
        f"{c['section']} -> {c['subsection']}"
    )

lengths = [
    len(c["text"].split())
    for c in chunks
]

print(max(lengths))