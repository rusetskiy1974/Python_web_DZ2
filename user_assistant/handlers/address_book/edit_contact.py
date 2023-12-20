from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.phone import Phone
from user_assistant.class_fields.date import Date
from user_assistant.class_fields.address import Address
from user_assistant.class_fields.mail import Mail
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console

FIELDS_CLASS = {'name': Name, 'birthday': Date, 'email': Mail, 'address': Address, 'phone': Phone}

def edit_contact(book: AddressBook, storage: Type[Storage]):
    while True:
        name = input_value('contact name', Name)
        record = book.find(name.value)
        if record:
            break
        else:
            Console.print_error('Input existing name')

    for field in FIELDS_CLASS.keys():  
            volume = input_value(f'new {field}', FIELDS_CLASS[field], True)
            
            if field == 'birthday' and volume:
                record.edit_birthday(volume)
            elif field == 'email' and volume:
                record.edit_email(volume)
            elif field == 'address' and volume:
                record.edit_address(volume)
            elif field == 'name' and volume:
                record.edit_name(volume)
            elif field == 'phone' and volume:
                while True:
                    phone_action = Console.input(f'Enter command - remove(r)/edit(e)/add(a): ')
                    if phone_action == 'r':
                        record.remove_phone(volume)
                        break
                    elif phone_action == 'a':
                        record.add_phone(volume)
                        break
                    elif phone_action == 'e':                 
                        old_phone = input_value('old phone number', Phone)
                        record.edit_phone(str(old_phone), str(volume)) 
                        break
                    Console.print_error('Unknown command. Enter command - remove(r)/edit(e)/add(a): ')
      
    Console.print_success(f'Contact {name} changed')
    storage.update(book.data.values())