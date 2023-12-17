from pathlib import Path

import commands
from handlers.address_book.add_contact import add_contact
from handlers.address_book.remove_contact import remove_contact
from handlers.address_book.edit_contact import edit_contact
from handlers.address_book.find_contact import find_contact
from handlers.address_book.show_birthday import show_birthday
from address_book.address_book import AddressBook
from storages.csv_storage import CSVStorage
from serializers.address_book.address_book_csv_serializer import AddressBookCSVSerializer


PATH = Path('databases') / Path('address_book.csv')
ADDRESS_BOOK_FIELDS = ['name', 'birthday', 'address', 'phones', 'mail']
storage = CSVStorage(PATH, AddressBookCSVSerializer, ADDRESS_BOOK_FIELDS)

book = AddressBook(storage.get())


def main():
    while True:
        user_input = input('Enter command: ').casefold()

        if user_input == commands.ADD_CONTACT:
            add_contact(book, storage)
            continue

        if user_input == commands.REMOVE_CONTACT:
            remove_contact()
            continue

        if user_input == commands.EDIT_CONTACT:
            edit_contact()
            continue

        if user_input == commands.FIND_CONTACT:
            find_contact()
            continue

        if user_input == commands.SHOW_BIRTHDAY:
            show_birthday(book)
            continue


if __name__ == '__main__':
    main()
