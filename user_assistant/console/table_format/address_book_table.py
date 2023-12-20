from user_assistant.address_book.address_book_record import AddressBookRecord


address_book_titles = ["😎 Name", "📧 Mail", "🏠 Address", "👑 Birthday", "📞 Phones"]


def get_address_book_row(record: AddressBookRecord):
    return [
        record.name.value,
        record.mail.value,
        record.address.value,
        str(record.birthday),
        ', '.join(list(map(lambda phone: phone.value, record.phones)))
    ]