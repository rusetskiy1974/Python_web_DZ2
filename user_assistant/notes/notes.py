from collections import UserDict
from .note_record import NoteRecord


class Notes(UserDict):
    def __init__(self, records: list[NoteRecord] = []):
        self.data = {record.id.value: record for record in records}

    def add_note(self, note: NoteRecord):
        self.data[note.id.value] = note


    def sort_by_tags(self):
        sorted_notes = sorted(self.data.values(), key=lambda note: ','.join(note.str_tags))
        return sorted_notes

    def delete(self, id: str):
        return self.data.pop(id, None)

    def find(self, id: str):
        return self.data.get(id, None)

    def search_by_author(self, searched_author: [str]):
        return [note for note in self.data.values() if note.str_author == searched_author]
    
    def search_by_tags(self, tag_name: str):
        matching_notes=[]
        for note in self.data.values():
            for tag in note.str_tags:
                if tag == tag_name.value:
                    matching_notes.append(note)
        return matching_notes
    
    def search_by_author(self, author: str):
        matching_notes=[]
        for note in self.data.values():
            if note.str_author == author.value:
                matching_notes.append(note)
        return matching_notes


    




