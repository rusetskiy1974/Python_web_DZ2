from typing import Type

from user_assistant.class_fields.author import Author
from user_assistant.class_fields.text import Text
from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.storages.storage import Storage
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row


NOTES_FIELDS = ['author', 'text']

def edit_note(notes: Notes, storage: Type[Storage]):
    Console.print_tip('Press “Enter” with empty value to skip')
    while True:
        value_id = Console.input(f'Enter note ID: ')
        existing_note = notes.find(value_id)
        print(type(existing_note))
        if existing_note:
            break
        else:
            Console.print_error('Input existing ID')

    while True:
        for field in NOTES_FIELDS:
            # new_volume = Console.input(f'Input new value for {field}: ')

            if field == 'author':
                try:
                    existing_note.edit_author(Author(Console.input(f'Input new value for {field}: ')))
                except Exception as error:
                    Console.print_error(error)
                    break    

            if field == 'text':
                try:
                    existing_note.edit_text(Text(Console.input(f'Input new value for {field}: ')))
                except Exception as error:
                    Console.print_error(error)
                    break 
        break       
    
    Console.print_table(f'Selected note chahged', note_titles, [get_notes_row(existing_note)])
    storage.update(notes.data.values())