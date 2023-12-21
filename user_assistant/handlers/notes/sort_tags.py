from user_assistant.console.console import Console
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row
from user_assistant.notes.notes import Notes

def sort_tags(notes: Notes):
    result = (notes.sort_by_tags())
    print(type(result), result)
    result_notes = notes.search_by_author(author)

    if result_notes:
        Console.print_table(f"Notes found for tag: {author}", note_titles, list(map(get_notes_row,result_notes)))

    if result is not None:
        return Console.print_table(f'Sorted note', note_titles, [get_notes_row(result)])


     