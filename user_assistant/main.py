from pathlib import Path


from .handlers.address_book.add_contact import add_contact
from .handlers.address_book.remove_contact import remove_contact
from .handlers.address_book.edit_contact import edit_contact
from .handlers.address_book.find_contact import find_contact
from .handlers.address_book.show_birthday import show_birthday
from .handlers.address_book.show_all_contacts import show_all_contacts
from .handlers.address_book.search_contact import search_contacts
from .handlers.address_book.add_phone import add_phone
from .handlers.address_book.edit_phone import edit_phone
from .handlers.address_book.remove_phone import remove_phone
from .handlers.sort_file.sort_file import sort_files
from .handlers.do_exit import do_exit

from .address_book.address_book import AddressBook
from .storages.csv_storage import CSVStorage
from .serializers.address_book.address_book_csv_serializer import AddressBookCSVSerializer

from .notes.notes import Notes
from .serializers.notes.notes_csv_serializer import NotesCSVSerializer
from .handlers.notes.add_note import add_note
from .handlers.notes.find_note import find_note
from .handlers.notes.remove_note import remove_note
from .handlers.notes.search_notes_by_author import search_notes_by_author
from .handlers.notes.search_notes_by_tag import search_notes_by_tag
from .handlers.notes.edit_note import edit_note
from .handlers.notes.sort_notes_by_tags import sort_notes_by_tags
from .handlers.notes.sort_notes_by_author import sort_notes_by_author
from .handlers.notes.remove_tags import remove_tags
from .handlers.notes.add_tags import add_tags
from .handlers.greeting import greeting
from .handlers.notes.show_all_notes import show_all_notes
from .handlers.help import help

from .console.console import Console

STORAGE_PATH = Path('.') / Path('databases')

ADDRESS_BOOK_FIELDS = ['name', 'birthday', 'address', 'phones', 'mail', 'updated_at', 'created_at']
NOTE_FIELDS = ['author', 'text', 'tags', 'id', 'updated_at', 'created_at']

address_book_storage = CSVStorage(STORAGE_PATH, 'address_book.csv', AddressBookCSVSerializer, ADDRESS_BOOK_FIELDS)
book = AddressBook(address_book_storage.get())

notes_storage = CSVStorage(STORAGE_PATH, 'notes.csv', NotesCSVSerializer, NOTE_FIELDS)
notes = Notes(notes_storage.get())

choice ={
        'add_contact': [add_contact, (book, address_book_storage)],
        'remove_contact': [remove_contact, [book, address_book_storage]],
        'edit_contact': [edit_contact, [book, address_book_storage]],
        'find_contact': [find_contact,[book]],
        'show_birthday': [show_birthday,[book]],
        'show_all_contacts': [show_all_contacts,[book]],
        'search_contacts': [search_contacts,[book]],
        'add_phone': [add_phone,[book, address_book_storage]],
        'edit_phone': [edit_phone,[book, address_book_storage]],
        'remove_phone': [remove_phone,[book, address_book_storage]],

        'add_note': [add_note, [notes, notes_storage]],
        'find_note': [find_note, [notes]],
        'show_all_notes': [show_all_notes, [notes]],
        'remove_note': [remove_note, [notes, notes_storage]],
        'search_notes_by_tag': [search_notes_by_tag, [notes]],
        'search_notes_by_author': [search_notes_by_author, [notes]],
        'edit_note': [edit_note, [notes, notes_storage]],
        'sort_notes_by_tags': [sort_notes_by_tags, [notes]],
        'sort_notes_by_author': [sort_notes_by_author, [notes]],
        'remove_tags': [remove_tags,[notes, notes_storage]],
        'add_tags': [add_tags,[notes, notes_storage]],
        
        'sort_files': [sort_files],
        'help': [help],
        'exit': [do_exit],
        'close': [do_exit]
    }

prompts = list([key for key in choice.keys()])

class ChoiceHandler:
    def __init__(self, choice) -> None:
        self.choice = choice
       
    def get_handler(self, handler):
        if handler in self.choice.keys():
            if len(self.choice[handler]) == 1:
                return self.choice[handler][0]()
            if len(self.choice[handler][1]) > 1:
                return self.choice[handler][0](self.choice[handler][1][0], self.choice[handler][1][1]) 
            else:
                return self.choice[handler][0](self.choice[handler][1][0])
        else:
             Console.print_tip('Enter [bold deep_sky_blue1]help[/] to see all possible commands') 

       
def main():
    greeting()
    handler = ChoiceHandler(choice)

    while True:
        user_input = Console.input('Enter command: ', prompts).casefold().strip()
        handler.get_handler(user_input)
         
              
        