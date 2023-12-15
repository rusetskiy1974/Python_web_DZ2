from class_fields.phone import Phone
from class_fields.name import Name
from class_fields.date import Date
from datetime import date


class AddressBookRecord:
    def __init__(self, name: Name, birthday: Date, phones: list[Phone] = []):
        self.name = name
        self.birthday = birthday
        self.phones = phones

    def __str__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"

    def __repr__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

        return self.phones

    def remove_phone(self, phone: str):
        self.phones = list(filter(lambda item: item.value != phone, self.phones))

        return self.phones

    def edit_phone(self, old_phone, new_phone):
        idx = self.phones.index(old_phone)
        self.phones[idx].value = new_phone

        return self.phones

    def find_phone(self, phone: str):
        phones = list(filter(lambda item: item.value == phone, self.phones))

        return phones[0] if len(phones) > 0 else None

    def days_to_birthday(self):
        today = date.today()
        closest_birthday = date(year=today.year, month=self.birthday.value.month, day=self.birthday.value.day)

        if today <= closest_birthday:
            return (closest_birthday - today).days

        closest_birthday.replace(year=closest_birthday.year + 1)

        return (closest_birthday - today).days

