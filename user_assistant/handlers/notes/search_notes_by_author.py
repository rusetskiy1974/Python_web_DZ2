from typing import Type

from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.class_fields.author import Author
from user_assistant.handlers.input_value import input_value



def search_notes_by_author(notes: Notes):
    author = input_value('author', Author)
    result_notes = notes.search_by_author(author)

    if result_notes:
        Console.print_success(f"Notes found for author: {author}")
        for note in result_notes:
            Console.print_success(f"Note ID: {note.id.value}, Author: {note.author.value}, Text: {note.text.value}, Tags: {', '.join(note.str_tags)}")
    else:
        Console.print_error(f"No notes found for the specified author: {author}")