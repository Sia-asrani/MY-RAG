import json


def export_chunks(chunks, output_path):

    with open(output_path, "w", encoding="utf-8") as f:

        json.dump(
            [chunk.to_dict() for chunk in chunks],
            f,
            indent=2,
            ensure_ascii=False
        )