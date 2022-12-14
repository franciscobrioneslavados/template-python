import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from domain.todo import TodoEntry
from domain.todo.repository import ITodoEntryRepository


class TodoEntryNotFound(Exception):
    pass


@dataclass
class TodoEntryPickleRepository(ITodoEntryRepository):
    storage_dir: str

    def get(self, entry_id: str) -> TodoEntry:
        try:
            entry: TodoEntry
            with open(Path(self.storage_dir) / entry_id, mode="rb") as entry_file:
                entry = pickle.load(entry_file)
            return entry
        except Exception:
            raise TodoEntryNotFound()

    def add(self, entry: TodoEntry) -> None:
        with open(Path(self.storage_dir) / entry.id, mode="wb") as entry_file:
            pickle.dump(entry, entry_file)

    def get_all(self, search: Optional[str]) -> list[TodoEntry]:
        entries: list[TodoEntry] = []
        for entry_file_path in Path(self.storage_dir).iterdir():
            with open(entry_file_path, mode="rb") as entry_file:
                entry: TodoEntry = pickle.load(entry_file)
                if search:
                    if search in entry.content or search in entry.tags:
                        entries.append(entry)
                else:
                    entries.append(entry)
        return entries