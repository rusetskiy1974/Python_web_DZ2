#  TODO Add formatted output
def search_contact(book):
    while True:
        string = input(f'Input keyword for name or phone :')
        if string:
            break
        print('Value is missing, try agane')

    result = book.search(string)

    if result:
        for record in result:
            print(record)
         
    else:
        print(f'There is no any contact with keyword: {string}')