from user_assistant.console.console import Console

def show_all(book):
    for value in book.data.values():
        Console.print_success(value)