from datetime import datetime
from typing import List

class Note:
    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body
        self.created_at = datetime.now()
        self.tags: List[str] = []
