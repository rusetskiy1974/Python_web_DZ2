from serializers.serializer import Serializer
from address_book.address_book_record import AddressBookRecord
from validations import date_validation
from class_fields.name import Name
from class_fields.date import Date
from class_fields.phone import Phone

class AddressBookCSVSerializer(Serializer):
    PHONE_SEPARATOR = '|'

    @classmethod
    def serialize(cls, record):
        return {
            "phones": cls.PHONE_SEPARATOR.join(list(map(lambda phone: phone.value, record.phones))),
            "name": record.name.value,
            "birthday": str(record.birthday.value)
        }


    @classmethod
    def deserialize(cls, record):
        phone_list = record['phones'].split(cls.PHONE_SEPARATOR) if len(record['phones']) >= 10 else []
        phones = list(map(lambda phone: Phone(phone), phone_list))
        print('!!!deserialize!!!', record['birthday'])

        birthday = Date(record['birthday']) if date_validation(record['birthday']) is not None else None

        return AddressBookRecord(Name(record['name']), None, phones)
