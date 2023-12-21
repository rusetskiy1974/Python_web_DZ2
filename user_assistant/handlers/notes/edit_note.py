from typing import Type

from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.storages.storage import Storage
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row


def edit_note(notes: Notes, storage: Type[Storage]):
    Console.print_tip('Press “Enter” with empty value to skip')
    while True:
        value_id = Console.input(f'Enter note ID: ')
        existing_note = notes.find(value_id)
        if existing_note:
            break
        else:
            Console.print_error('Input existing ID')

    result = notes.find(value)

    if result is not None:


