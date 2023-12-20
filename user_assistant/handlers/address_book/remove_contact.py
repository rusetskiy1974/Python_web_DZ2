from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row


def remove_contact(book: AddressBook, storage: Type[Storage]):
    name = input_value('name', Name)
    record = book.find(name.value)
    
    if record is not None:
        book.delete(name.value)
        storage.update(book.data.values())
        Console.print_success(f'Contact {name} removed')
        return

    Console.print_table('Removed contact', address_book_titles, [get_address_book_row(record)])
