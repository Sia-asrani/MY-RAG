"""defines the chunk class - json structure for better parsing"""

from dataclasses import dataclass, asdict

@dataclass
class Chunk:

    id: str

    document: str

    page: int

    major_section: str | None = None

    section: str | None = None

    subsection: str | None = None

    subsection_id: str | None = None

    knowledge_type: str | None = None

    text: str = ""

    def to_dict(self):
        return asdict(self)