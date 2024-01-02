from typing import Type

from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.class_fields.author import Author
from user_assistant.handlers.input_value import input_value
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row



def search_notes_by_author(notes: Notes):
    prompts = list(el.author.value.casefold().strip() for el in  notes.data.values())
    author = input_value('author', Author, prompts=prompts)
    result_notes = notes.search_by_author(author.value)
    Console.print_table(f"Notes found for tag: {author}", note_titles, list(map(get_notes_row,result_notes)))
