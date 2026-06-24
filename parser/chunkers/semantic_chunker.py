"""
Creates semantic chunks for narrative content.

Department descriptions
Mission statements
Features
Competencies

Splits text into manageable semantic blocks.
"""

from parser.chunk import Chunk


def semantic_split(
    text,
    max_words=250
):

    words = text.split()

    chunks = []

    for i in range(
        0,
        len(words),
        max_words
    ):

        chunks.append(
            " ".join(
                words[i:i + max_words]
            )
        )

    return chunks


def create_semantic_chunks(
    text,
    section_name,
    page,
    start_id
):

    output = []

    parts = semantic_split(text)

    counter = start_id

    for part in parts:

        output.append(

            Chunk(
                id=f"chunk_{counter}",
                document="MUJ Academic Handbook",
                page=page,
                chunk_type="semantic",
                section=section_name,
                text=part
            )

        )

        counter += 1

    return output