from user_assistant.address_book.address_book import AddressBook
from user_assistant.console.console import Console

def show_all_contacts(book: AddressBook):
    for value in book.data.values():
        Console.print_success(value)
         