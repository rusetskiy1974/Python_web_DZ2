from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.notes.note_record import NoteRecord
from user_assistant.class_fields.author import Author
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row

def remove_note(notes: Notes):
    value = Console.input('Input name or tag: ')
    result  = notes.find(value)
     
    if result is not None:
        notes.delete(value)
        return Console.print_table(f'Remove note', note_titles, [get_notes_row(result)])
    
    result = notes.search_by_tags([value])   
     
    if result != []:
        for record in result:
            notes.delete(record.author.value)
            Console.print_table(f'Remove notes', note_titles, [get_notes_row(record)])
        return 

    Console.print_error(f'There is no any notes named: {value}') 