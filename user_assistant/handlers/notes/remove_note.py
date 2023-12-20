from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row

def remove_note(notes: Notes):
    value = Console.input('Input name or teg :')
    result  = notes.find(value)

    if result is not None:
        result.delete(value)
        return Console.print_table(f'Remove note', note_titles, [get_notes_row(result)])
        
     