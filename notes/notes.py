
class Notes:

    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def search_by_tags(self, search_tags):
        result_notes = [note for note in self.notes if set(search_tags).issubset(note.tags)]
        return result_notes

    def sort_by_tags(self):
        sorted_notes = sorted(self.notes, key=lambda note: ','.join(note.tags))
        return sorted_notes

    def delete_note_by_index(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            print("Note deleted successfully.")
        else:
            print("Invalid note index.")

