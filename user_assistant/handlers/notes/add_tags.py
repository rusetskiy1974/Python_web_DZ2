from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.class_fields.tag import Tag
from user_assistant.handlers.input_value import input_value

def add_tags(notes: Notes):
    note_id = Console.input("Enter the ID of the note you want to tag: ")

    note = notes.find(note_id)
    if note is None:
        return Console.print_error(f"No note with ID: {note_id}")

    while True:
        tag_value = input_value("tag", Tag)
        note.add_tag(Tag(tag_value))

        if Console.input("Add anither tagг? (yes/no) ") != "yes":
            break

    Console.print_success(f"Tags have been successfully added to the note {note_id}")
