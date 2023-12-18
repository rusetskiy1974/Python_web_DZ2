from typing import Type

from address_book.address_book import AddressBook
from class_fields.name import Name
from handlers.address_book.add_contact import input_value
from storages.storage import Storage

def remove_contact(book: AddressBook, storage: Type[Storage]):
    name = input_value('name', Name)

    book.delete(str(name))
    storage.update(book.data.values())

    print(f'Contact {name} removed')
