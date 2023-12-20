from pathlib import Path

from . import commands as COMMANDS
from .handlers.address_book.add_contact import add_contact
from .handlers.address_book.remove_contact import remove_contact
from .handlers.address_book.edit_contact import edit_contact
from .handlers.address_book.find_contact import find_contact
from .handlers.address_book.show_birthday import show_birthday
from .handlers.address_book.show_all_contacts import show_all_contacts
from .handlers.address_book.search_contact import search_contact
from .handlers.sort_file.sort_file import sort_files
from .handlers.do_exit import do_exit

from .address_book.address_book import AddressBook
from .storages.csv_storage import CSVStorage
from .serializers.address_book.address_book_csv_serializer import AddressBookCSVSerializer

from .notes.notes import Notes
from .serializers.notes.notes_csv_serializer import NotesCSVSerializer
from .handlers.notes.add_note import add_note
from .handlers.notes.find_note import find_note
from .handlers.greeting import greeting
from .handlers.notes.show_all_notes import show_all_notes

from .console.console import Console

STORAGE_PATH = Path('') / Path('databases')
ADDRESS_BOOK_FIELDS = ['name', 'birthday', 'address', 'phones', 'mail']
NOTE_FIELDS = ['author', 'text', 'tags', 'id', 'created_at']

address_book_storage = CSVStorage(STORAGE_PATH, 'address_book.csv', AddressBookCSVSerializer, ADDRESS_BOOK_FIELDS)
book = AddressBook(address_book_storage.get())

notes_storage = CSVStorage(STORAGE_PATH, 'notes.csv', NotesCSVSerializer, NOTE_FIELDS)
notes = Notes(notes_storage.get())


def main():
    greeting()

    while True:

        user_input = Console.input('Enter command: ').casefold()

        if user_input == COMMANDS.ADD_CONTACT:
            add_contact(book, address_book_storage)
            continue

        if user_input == COMMANDS.REMOVE_CONTACT:
            remove_contact(book, address_book_storage)
            continue

        if user_input == COMMANDS.EDIT_CONTACT:
            edit_contact(book, address_book_storage)
            continue

        if user_input == COMMANDS.FIND_CONTACT:
            find_contact(book)
            continue

        if user_input == COMMANDS.SHOW_BIRTHDAY:
            show_birthday(book)
            continue

        if user_input == COMMANDS.SHOW_ALL_CONTACTS:
            show_all_contacts(book)
            continue

        if user_input == COMMANDS.SEARCH_CONTACT:
            search_contact(book)
            continue

        if user_input == COMMANDS.SORT_FILES:
            sort_files()
            continue

        if user_input in (COMMANDS.EXIT, COMMANDS.CLOSE):
            do_exit()
            break

        if user_input == COMMANDS.ADD_NOTE:
            add_note(notes, notes_storage)
            continue

        if user_input == COMMANDS.FIND_NOTE:
            find_note(notes)
            continue

        if user_input == COMMANDS.SHOW_ALL_NOTES:
            show_all_notes(notes)
            continue


if __name__ == '__main__':
    main()
