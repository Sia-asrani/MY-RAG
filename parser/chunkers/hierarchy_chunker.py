"""
Creates chunks from numbered handbook hierarchy.

4.8
4.8.1
4.8.2

Each leaf subsection becomes a chunk.
"""

from parser.chunk import Chunk


def create_hierarchy_chunk(
    chunk_id,
    page,
    section,
    subsection,
    subsection_id,
    text
):

    return Chunk(
        id=chunk_id,
        document="MUJ Academic Handbook",
        page=page,
        chunk_type="hierarchy",
        section=section,
        subsection=subsection,
        subsection_id=subsection_id,
        text=text
    )