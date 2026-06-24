"""defines the chunk class - redesigned structure for better parsing"""

from dataclasses import dataclass, asdict

@dataclass
class Chunk:

    id: str

    document: str

    page: int

    chunk_type: str

    major_section: str | None = None

    section: str | None = None

    subsection: str | None = None

    subsection_id: str | None = None

    metadata: dict | None = None

    text: str = ""

    def to_dict(self):
        return asdict(self)