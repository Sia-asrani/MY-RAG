"""
Hybrid chunking pipeline.

Supports:

1. Hierarchical chunks
2. Semantic chunks
3. Table chunks

Returns unified Chunk objects.
"""

import re

from parser.chunk import Chunk

from parser.chunk_router import (
    get_line_metadata
)

from parser.chunkers.semantic_chunker import (
    create_semantic_chunks
)

from parser.chunkers.table_chunker import (
    create_table_chunk
)


def build_chunks(pages):

    chunks = []

    chunk_counter = 1

    current_section = None

    current_subsection = None

    current_subsection_id = None

    hierarchy_buffer = []

    semantic_buffer = []

    semantic_title = None

    def is_noise_line(line):

        return bool(
            re.fullmatch(r"\d+", line)
            or re.fullmatch(r"[IVXLC]+", line)
            or re.fullmatch(r"[*_]{3,}", line)
        )

    def flush_hierarchy(page_num):

        nonlocal chunk_counter

        if not hierarchy_buffer:
            return

        text = " ".join(
            hierarchy_buffer
        ).strip()

        if not text:
            hierarchy_buffer.clear()
            return

        if (
            current_subsection
            and text == current_subsection
            and len(text.split()) <= 8
        ):
            hierarchy_buffer.clear()
            return

        chunks.append(

            Chunk(
                id=f"chunk_{chunk_counter}",
                document="MUJ Academic Handbook",
                page=page_num,
                chunk_type="hierarchy",
                section=current_section,
                subsection=current_subsection,
                subsection_id=current_subsection_id,
                text=text
            )

        )

        chunk_counter += 1

        hierarchy_buffer.clear()

    def flush_semantic(page_num):

        nonlocal chunk_counter

        if not semantic_buffer:
            return

        text = " ".join(
            semantic_buffer
        ).strip()

        if not text:
            return

        semantic_chunks = (
            create_semantic_chunks(
                text=text,
                section_name=semantic_title,
                page=page_num,
                start_id=chunk_counter
            )
        )

        chunks.extend(
            semantic_chunks
        )

        chunk_counter += len(
            semantic_chunks
        )

        semantic_buffer.clear()

    for page in pages:

        page_num = page["page"]

        lines = page["text"].split("\n")

        for raw_line in lines:

            line = raw_line.strip()

            if not line:
                continue

            if is_noise_line(line):
                continue

            info = get_line_metadata(
                line
            )

            line_type = info["type"]

            data = info["data"]

            # ==========================
            # HIERARCHY
            # ==========================

            if line_type == "hierarchy":

                flush_semantic(
                    page_num
                )

                semantic_title = None

                heading = data

                depth = heading["depth"]

                if depth > 1 and current_section is None:
                    continue

                if depth == 1:

                    flush_hierarchy(
                        page_num
                    )

                    current_section = (
                        heading["content"]
                    )

                    current_subsection = None

                    current_subsection_id = None

                    continue

                elif depth == 2:

                    flush_hierarchy(
                        page_num
                    )

                    current_subsection = (
                        heading["content"]
                    )

                    current_subsection_id = (
                        heading["number"]
                    )

                    hierarchy_buffer.append(
                        heading["content"]
                    )

                    continue

                elif depth >= 3:

                    flush_hierarchy(
                        page_num
                    )

                    current_subsection_id = (
                        heading["number"]
                    )

                    hierarchy_buffer.append(
                        heading["content"]
                    )

                    continue

            # ==========================
            # SEMANTIC
            # ==========================

            elif line_type == "semantic":

                flush_hierarchy(
                    page_num
                )

                flush_semantic(
                    page_num
                )

                current_section = None

                current_subsection = None

                current_subsection_id = None

                semantic_title = (
                    data["title"]
                )

                semantic_buffer = []

                continue

            # ==========================
            # TABLE
            # ==========================

            elif line_type == "table":

                table_chunk = (
                    create_table_chunk(
                        line=line,
                        page=page_num,
                        chunk_id=chunk_counter
                    )
                )

                if table_chunk:

                    chunks.append(
                        table_chunk
                    )

                    chunk_counter += 1

                continue

            # ==========================
            # NORMAL TEXT
            # ==========================

            else:

                if current_subsection_id:

                    hierarchy_buffer.append(
                        line
                    )

                elif semantic_title:

                    semantic_buffer.append(
                        line
                    )

    flush_hierarchy(page_num)

    flush_semantic(page_num)

    print("\n" + "=" * 80)

    print(
        f"TOTAL CHUNKS: {len(chunks)}"
    )

    hierarchy_count = sum(
        1
        for c in chunks
        if c.chunk_type == "hierarchy"
    )

    semantic_count = sum(
        1
        for c in chunks
        if c.chunk_type == "semantic"
    )

    table_count = sum(
        1
        for c in chunks
        if c.chunk_type == "course"
    )

    print(
        f"Hierarchy: {hierarchy_count}"
    )

    print(
        f"Semantic: {semantic_count}"
    )

    print(
        f"Table: {table_count}"
    )

    print("=" * 80)

    return chunks
