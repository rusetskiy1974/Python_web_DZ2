from user_assistant.console.console import Console

def search_contact(book):
    while True:
        string = Console.input(f'Input contact name or phone:')
        if string:
            break
        Console.print_error('Value is missing, try agane')

    result = book.search(string)

    if result:
        for record in result:
            Console.print_success(record)
         
    else:
        Console.print_error(f'There is no any contact by your request')