from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.date import Date
from user_assistant.class_fields.address import Address
from user_assistant.class_fields.mail import Mail
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row


FIELDS_CLASS = {'name': Name, 'birthday': Date, 'email': Mail, 'address': Address}


def edit_contact(book: AddressBook, storage: Type[Storage]):
    Console.print_tip('Press “Enter” with empty value to skip')
    while True:
        name = input_value('contact name', Name, True)
        
        if name:
            record = book.find(name.value)
            if record:
                break
            else:
                Console.print_error('Input existing name')

        else:
            return        

    for field in FIELDS_CLASS.keys():  
            volume = input_value(f'new {field}', FIELDS_CLASS[field], True)
            
            if field == 'birthday' and volume:
                record.edit_birthday(volume)
            elif field == 'email' and volume:
                record.edit_email(volume)
            elif field == 'address' and volume:
                record.edit_address(volume)
            elif field == 'name' and volume:
                book.delete(str(record.name))
                record.edit_name(volume)
                book.add(record)
            
      
    storage.update(book.data.values())

    Console.print_table('Updated contact', address_book_titles, [get_address_book_row(record)])
