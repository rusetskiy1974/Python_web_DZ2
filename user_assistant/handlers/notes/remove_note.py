from typing import Type

from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.handlers.input_value import input_value
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row
from user_assistant.storages.storage import Storage

def remove_note(notes: Notes, storage: Type[Storage]):
    prompts = list(el.id.value.casefold().strip() for el in  notes.data.values())

    value = input_value(f'note ID', str, prompts=prompts)
    
    result = notes.find(value)

    if result is not None:
       notes.delete(value)
       storage.update(notes.data.values())
       return Console.print_table(f'Remove note', note_titles, [get_notes_row(result)])
       
    Console.print_error(f'There is no any notes named: {value}') 