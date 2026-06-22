from parser.chunk import Chunk
from parser.hierarchy_detector import get_heading


def build_chunks(pages):

    chunks = []

    subsection_lookup = {}

    current_section = None
    current_chunk_number = None

    buffer = []

    chunk_counter = 1

    def flush_chunk(page_num):

        nonlocal chunk_counter

        if current_chunk_number is None:
            return

        text = " ".join(buffer).strip()

        if not text:
            return

        parent_number = ".".join(
            current_chunk_number.split(".")[:-1]
        )

        subsection_name = subsection_lookup.get(
            parent_number,
            "UNKNOWN"
        )

        chunks.append(
            Chunk(
                id=f"chunk_{chunk_counter}",
                document="MUJ Academic Handbook",
                page=page_num,
                section=current_section,
                subsection=subsection_name,
                subsection_id=current_chunk_number,
                text=text
            )
        )

        chunk_counter += 1

    for page in pages:

        page_num = page["page"]

        lines = page["text"].split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            heading = get_heading(line)

            if heading:

                depth = heading["depth"]

                # --------------------
                # DEPTH 1
                # --------------------

                if depth == 1:

                    current_section = heading["content"]

                    continue

                # --------------------
                # DEPTH 2
                # --------------------

                elif depth == 2:

                    subsection_lookup[
                        heading["number"]
                    ] = heading["content"]

                    continue

                # --------------------
                # DEPTH 3
                # --------------------

                elif depth == 3:

                    flush_chunk(page_num)

                    buffer.clear()

                    current_chunk_number = heading["number"]

                    buffer.append(
                        heading["content"]
                    )

                    continue

                # --------------------
                # DEPTH 4+
                # --------------------

                elif depth >= 4:

                    buffer.append(
                        f"{heading['number']} {heading['content']}"
                    )

                    continue

            buffer.append(line)

    flush_chunk(page_num)

    return chunks