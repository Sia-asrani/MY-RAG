"""
Routes lines to the correct chunking strategy.

Possible outputs:

hierarchy
semantic
table
text
"""

from parser.detectors.hierarchy_det import get_heading
from parser.detectors.section_det import detect_section
from parser.detectors.table_det import is_table_row


def detect_chunk_type(line):

    if get_heading(line):
        return "hierarchy"

    if is_table_row(line):
        return "table"

    if detect_section(line):
        return "semantic"

    return "text"


def get_line_metadata(line):

    hierarchy = get_heading(line)

    if hierarchy:

        return {
            "type": "hierarchy",
            "data": hierarchy
        }

    semantic = detect_section(line)

    if semantic:

        return {
            "type": "semantic",
            "data": semantic
        }

    if is_table_row(line):

        return {
            "type": "table",
            "data": line
        }

    return {
        "type": "text",
        "data": line
    }