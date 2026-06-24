"""
Creates structured chunks from curriculum tables.

Example:

HA1101 Food Production Foundation - I

becomes

{
    course_code: HA1101
    course_name: Food Production Foundation - I
}
"""

import re

from parser.chunk import Chunk

COURSE_PATTERN = re.compile(
    r"^([A-Z]{2,4}\s?\d{4}):?\s+(.+)$"
)


def create_table_chunk(
    line,
    page,
    chunk_id
):

    match = COURSE_PATTERN.match(
        line.strip()
    )

    if not match:
        return None

    code = match.group(1).replace(
        " ",
        ""
    )

    name = match.group(2)

    return Chunk(
        id=f"chunk_{chunk_id}",
        document="MUJ Academic Handbook",
        page=page,
        chunk_type="course",
        section="Curriculum",
        metadata={
            "course_code": code,
            "course_name": name
        },
        text=f"{code} {name}"
    )
