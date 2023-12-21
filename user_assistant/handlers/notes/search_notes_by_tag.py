from typing import Type

from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.class_fields.tag import Tag
from user_assistant.handlers.input_value import input_value




def search_notes_by_tag(notes: Notes):
    tag = input_value('tag', Tag)
    result_notes = notes.search_by_tags(tag)

    if result_notes:
        Console.print_success(f"Notes found for tag: {tag}")
        for note in result_notes:
            Console.print_success(f"Note ID: {note.id.value}, Author: {note.author.value}, Text: {note.text.value}, Tags: {', '.join(note.str_tags)}")
    else:
        Console.print_error(f"No notes found for the specified tag: {tag}")