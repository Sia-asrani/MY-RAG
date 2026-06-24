"""
Detects numbered hierarchical headings such as:

1. ACADEMIC PROGRAMMES
4.8 Attendance Requirements
4.8.2 Attendance below 75%

Returns structured heading metadata or None.
"""

import re

HEADING_PATTERN = re.compile(
    r"^(\d+(?:\.\d+)*)(\.)?\s+(.+)$"
)

COURSE_CODE_PATTERN = re.compile(
    r"^[A-Z]{2,4}\s?\d{4}:?$"
)


def _is_valid_heading(number, separator, content):

    depth = len(number.split("."))

    content = content.strip()

    if len(content) < 3:
        return False

    # only numbered handbook hierarchy

    if depth == 1:

        words = content.split()

        if separator != ".":
            return False

        if len(words) > 8:
            return False

        if "," in content:
            return False

        if COURSE_CODE_PATTERN.match(content):
            return False

        alpha_count = sum(
            c.isalpha()
            for c in content
        )

        if alpha_count == 0:
            return False

        uppercase_ratio = (
            sum(c.isupper() for c in content)
            / alpha_count
        )

        # MUST BE MOSTLY UPPERCASE

        if uppercase_ratio < 0.7:
            return False

        return True

    return True

def get_heading(line):

    line = line.strip()

    if not line:
        return None

    match = HEADING_PATTERN.match(line)

    if not match:
        return None

    number = match.group(1)

    separator = match.group(2)

    content = match.group(3).strip()

    if not _is_valid_heading(
        number,
        separator,
        content
    ):
        return None

    return {
        "number": number,
        "depth": len(number.split(".")),
        "content": content
    }
