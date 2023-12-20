from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console


def find_note(notes: Notes):
    value = Console.input(f'Enter note id: ')

    result = notes.find(value)

    if result is not None:
        return Console.print_success(result)

    Console.print_error(f'There is no any contact named: {value}')