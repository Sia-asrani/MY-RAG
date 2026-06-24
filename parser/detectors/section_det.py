"""
Detects unnumbered document sections.

Examples:

Department of Hotel Management
KEY FEATURES
CORE COMPETENCIES

Used for semantic chunking.
"""

import re

DEPARTMENT_PATTERN = re.compile(
    r"^Department of .+",
    re.IGNORECASE
)

SCHEME_PATTERN = re.compile(
    r"^Bachelor of .+ Scheme \d{4}$",
    re.IGNORECASE
)

# ALL_CAPS_PATTERN = re.compile(
#     r"^[A-Z\s&\-]{3,}$"
# )


def detect_section(line):

    line = line.strip()

    if not line:
        return None

    if DEPARTMENT_PATTERN.match(line):

        return {
            "type": "department",
            "title": line
        }
        
    if SCHEME_PATTERN.match(line):
        return {
        "type": "scheme",
        "title": line}
    return None
