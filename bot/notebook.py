from typing import List, Optional
from bot.note import Note

class Notebook:
    def __init__(self):
        self._notes: List[Note] = []

    @property
    def notes(self) -> List[Note]:
        return self._notes

    def add(self, note: Note) -> None:
        self._notes.append(note)

    def find(self, query: str) -> List[Note]:
        q = query.lower()
        return [n for n in self._notes if q in n.title.lower() or q in n.body.lower()]

    def find_by_title(self, title: str) -> Optional[Note]:
        for note in self._notes:
            if note.title == title:
                return note
        return None

    def edit(self, title: str, new_body: str) -> bool:
        note = self.find_by_title(title)
        if note is None:
            return False
        note.body = new_body
        return True

    def delete(self, title: str) -> bool:
        note = self.find_by_title(title)
        if note is None:
            return False
        self._notes.remove(note)
        return True
