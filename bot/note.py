from datetime import datetime
from typing import List


class Note:
    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body
        self.created_at = datetime.now()
        self.tags: List[str] = []

    def add_tag(self, tag: str) -> None:
        normalized_tag = tag.strip().lower()
        if not normalized_tag:
            raise ValueError("Tag cannot be empty.")
        if normalized_tag not in self.tags:
            self.tags.append(normalized_tag)