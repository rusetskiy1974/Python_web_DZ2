from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.class_fields.tag import Tag
from user_assistant.handlers.input_value import input_value

def add_tags(notes: Notes):
    note_id = Console.input("Введіть ID нотатки, до якої потрібно додати теги: ")

    note = notes.find(note_id)
    if note is None:
        return Console.print_error(f"Немає нотатки з ID: {note_id}")

    while True:
        tag_value = input_value("tag", Tag)
        note.add_tag(Tag(tag_value))

        if Console.input("Додати ще один тег? (так/ні) ") != "так":
            break

    Console.print_success(f"Теги успішно додані до нотатки {note_id}")
