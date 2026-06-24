"""
Detects curriculum table rows.

Examples:

HA1101 Food Production Foundation - I
CS2104 Data Structures
MA2201 Statistics

Used for table-aware chunking.
"""

import re

COURSE_PATTERN = re.compile(
    r"^[A-Z]{2,4}\s?\d{4}:?\s+.+"
)


def is_table_row(line):

    line = line.strip()

    return bool(
        COURSE_PATTERN.match(line)
    )
