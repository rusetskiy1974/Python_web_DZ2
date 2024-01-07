from user_assistant.console.console import Console


column_titles = ['Command', 'Fields', 'Description']


address_book_documentation = [
    ['add_contact', 'name, birthday, phone, address, mail', 'Create a new contact'],
    ['edit_contact', 'name, birthday, address, mail', 'Edit an existing contact'],
    ['remove_contact', 'name', 'Remove an existing contact'],
    ['find_contact', 'name', 'Find a contact by name'],
    ['add_phone', 'name, phone', 'Add a new phone for contact'],
    ['edit_phone', 'name', 'Edit an existing phone of contact'],
    ['remove_phone', 'name', 'Remove an existing phone of contact'],
    ['search_contacts', 'name or phone', 'Search contacts by name or phone'],
    ['show_all_contacts', '', 'Show all contacts'],
    ['show_birthday',  'days', 'Show contacts who birthdays will be in period of entered days'],
]

notes_documentation = [
    ['add_note', 'author, text, tag', 'Create a new note'],
    ['edit_note', 'id, author, text', 'Edit an existing note'],
    ['remove_note', 'id', 'Remove an existing contact'],
    ['find_note', 'id', 'Find a note by id'],
    ['add_tags', 'id, tags', 'Add tags of note by id'],
    ['remove_tags', 'id, tags', 'Remove tags of note by id'],
    ['show_all_notes', '', 'Show all notes'],
    ['search_notes_by_tag', 'tag', 'Search notes by tag'],
    ['search_notes_by_author', 'author', 'Search notes by author'],
    ['sort_notes_by_tags', '', 'Sort notes by tags'],
    ['sort_notes_by_author', '', 'Sort notes by author'],
]

sort_files_documentation = [
    ['sort_files', 'folder', 'Sorting files inside folder by categories: music, image, video, documents'],
]

additional_commands_documentation = [
    ['exit', 'Exit from user assistant'],
    ['close', 'Exit from user assistant'],
    ['help', 'Show documentations'],
]
def help():
    Console.print_table('Address book', column_titles, address_book_documentation)
    Console.print_table('Notes', column_titles, notes_documentation)
    Console.print_table('Sort files', column_titles, sort_files_documentation)
    Console.print_table('Additionals', list(filter(lambda title: title != 'Fields', column_titles)), additional_commands_documentation)