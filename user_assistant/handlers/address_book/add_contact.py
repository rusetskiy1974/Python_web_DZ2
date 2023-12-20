from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.phone import Phone
from user_assistant.class_fields.date import Date
from user_assistant.class_fields.address import Address
from user_assistant.class_fields.mail import Mail
from user_assistant.address_book.address_book_record import AddressBookRecord
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row


def add_contact(book: AddressBook, storage: Type[Storage]):

    name = input_value('name', Name)
    date = input_value('date birthday', Date )
    mail = input_value('email', Mail)
    address = input_value('address', Address)
    phone = input_value('phone', Phone)

    record = AddressBookRecord(name= name, birthday= date, mail= mail, address= address,  phones= [phone])
    book.add(record)
    storage.update(book.data.values())

    Console.print_table('Created contact', address_book_titles, [get_address_book_row(record)])
