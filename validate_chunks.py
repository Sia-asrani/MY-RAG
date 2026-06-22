"""tests the generated chunks.json if they adhere to the format, and relevent chunking"""
import json

with open(
    "output/chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)

print("Total Chunks:", len(chunks))

print()

for chunk in chunks:

    if chunk["subsection"] == "UNKNOWN":

        print("UNKNOWN FOUND")

        print(chunk["subsection_id"])

        break