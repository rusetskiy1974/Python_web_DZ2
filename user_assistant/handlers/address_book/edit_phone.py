from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.phone import Phone
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row

def edit_phone(book: AddressBook, storage: Type[Storage]):
    while True:
        name = input_value('contact name', Name)
        record = book.find(name.value)
        if record:
            break
        else:
            Console.print_error('Input existing name')

    phone = input_value('phone', Phone) 

    if record.find_phone(phone):
        new_phone = input_value('phone', Phone) 
        record.edit_phone(phone, new_phone)
        storage.update(book.data.values()) 
        Console.print_table('Updated phone contact', address_book_titles, [get_address_book_row(record)])
    else:
        Console.print_error(f'Number {phone} is missing from the contact {name}')    