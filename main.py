import commands
from handlers.address_book.add_contact import add_contact
from handlers.address_book.remove_contact import remove_contact


def main():
    while True:
        user_input = input('Enter command: ').casefold()

        if user_input == commands.ADD_CONTACT:
            add_contact()
            continue

        if user_input == commands.REMOVE_CONTACT:
            remove_contact()
            continue

if __name__ == '__main__':
    main()
