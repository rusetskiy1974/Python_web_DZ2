from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value

def remove_contact(book: AddressBook, storage: Type[Storage]):
    name = input_value('name', Name)
    result = book.find(name.value)
    
    if result is not None:
        book.delete(str(name))
        storage.update(book.data.values())
        print(f'Contact {name} removed')
        return
    
    print(f'There is no any contact named: {name}')
    

