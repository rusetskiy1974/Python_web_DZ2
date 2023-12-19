from typing import Type

from user_assistant.notes.note_record import NoteRecord
from user_assistant.class_fields.text import Text
from user_assistant.class_fields.author import Author
from user_assistant.class_fields.tag import Tag
from user_assistant.handlers.input_value import input_value
from user_assistant.notes.notes import Notes
from user_assistant.storages.storage import Storage
from user_assistant.console.console import Console


def add_note(notes: Notes, storage: Type[Storage]):
    author = input_value('author',Author)
    text = input_value('text',Text)
    tag = input_value('tag',Tag)

    note_record = NoteRecord(author=author,text=text,tags=[tag])
    notes.add_note(note_record)
    storage.update(notes.data.values())

    Console.print_success(f'Note {note_record.id.value} was added')