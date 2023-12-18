from prettytable import PrettyTable
from note_record import NoteRecord

class Notes:

    # список для зберігання нотаток
    def __init__(self):
        self.notes = []

    # додати нотатку
    def add_note(self, author, text, tags):
        new_note =  NoteRecord(author, text, tags)
        self.notes.append(new_note)

    # пошук за тегами
    def search_by_tags(self, search_tags):
        result_notes = [note for note in self.notes if set(search_tags).issubset(note.tags)]
        if result_notes:
            table = PrettyTable(['Index', 'Author', 'Text', 'Tags', 'Date'])
            for i, note in enumerate(result_notes):
                table.add_row([i, note.author, note.text, ', '.join(note.tags), note.date.strftime('%Y-%m-%d %H:%M:%S')])
            print(table)
        else:
            print("No notes found with the specified tags.")

    # сортування за тегами по алфавіту
    def sort_by_tags(self):
        sorted_notes = sorted(self.notes, key=lambda note: ','.join(note.tags))
        table = PrettyTable(['Index', 'Author', 'Text', 'Tags', 'Date'])
        for i, note in enumerate(sorted_notes):
            table.add_row([i, note.author, note.text, ', '.join(note.tags), note.date.strftime('%Y-%m-%d %H:%M:%S')])
        print(table)

    # видалення нотатки
    def delete_note_by_index(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            print("Note deleted successfully.")
        else:
            print("Invalid note index.")

    # Виведення нотаток таблицею
    def display_notes_table(self):
            table = PrettyTable(['Index', 'Author', 'Text', 'Tags', 'Date'])
            for i, note in enumerate(self.notes):
                table.add_row([i, note.author, note.text, ', '.join(note.tags), note.date.strftime('%Y-%m-%d %H:%M:%S')])

            print(table)