from user_assistant.console.console import Console

def show_birthday(book):
    while True:
        try:
            days = int(Console.input(f'Enter volume days :'))
            if days in range(1,365):
                break
            else:
                Console.print_error('Days may be in interval 1-365')
                continue
        except:
           Console.print_error(ValueError('Days may be integer volume'))

    result = book.show_birthday(days)
    for record in result:
        Console.print_success(record)