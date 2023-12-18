from typing import Type

from address_book.address_book import AddressBook
from class_fields.name import Name
from class_fields.phone import Phone
from class_fields.date import Date
from class_fields.address import Address
from class_fields.mail import Mail
from address_book.address_book_record import AddressBookRecord
from storages.storage import Storage


def input_value(value, class_field):
    while True:
        result = input(f'Enter {value}: ')
        try:
            result = class_field(result)
            return result
        except Exception as error:
            print(error)
            continue


def add_contact(book: AddressBook, storage: Type[Storage]):

    name = input_value('name', Name)
    date = input_value('date birthday', Date )
    mail = input_value('email', Mail)
    address = input_value('address', Address)
    phone = input_value('phone', Phone)

    record = AddressBookRecord(name= name, birthday= date, mail= mail, address= address,  phones= [phone])
    book.add(record)
    storage.update(book.data.values())

    print(f'Contact {name.value} was added')
