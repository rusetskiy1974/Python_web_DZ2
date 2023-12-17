from address_book.address_book_record import AddressBookRecord

def show_birthday(book):
    while True:
        print ('Enter volume days >>>', end=' ' )
        try:
            days = int(input())
            if days <= 365:
                break
            else:
                print('Days may be in interval 1-365')
        except:
            ValueError('Days may be integer volume')
            

    for record in book:
        # if record.days_to_birthday() <= days:
            print(type(record))
            # print(record)
    