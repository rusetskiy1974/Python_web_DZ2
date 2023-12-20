from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console


# TODO Update printing result
def find_contact(book: AddressBook):
    name = input_value('name', Name)

    result = book.find(name.value)

    if result is not None:
        return Console.print_success(result)

    Console.print_error(f'There is no any contact named: {name}')