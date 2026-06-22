import re

HEADING_PATTERN = re.compile(
    r"^(\d+(?:\.\d+)*)\.?\s+(.+)$"
)


def get_heading(line):

    line = line.strip()

    if not line:
        return None

    match = HEADING_PATTERN.match(line)

    if not match:
        return None

    number = match.group(1)

    content = match.group(2)

    depth = len(number.split("."))

    return {
        "number": number,
        "depth": depth,
        "content": content
    }