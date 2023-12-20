from user_assistant.console.console import Console

def show_all_contacts(book):
    for value in book.data.values():
        Console.print_success(value)
         