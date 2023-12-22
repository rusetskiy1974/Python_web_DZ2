from phonenumbers import is_valid_number, parse
from .field import Field


class Phone(Field):
    PHONE_FORMAT_EXAMPLE = '+380931234567';

    def __eq__(self, other: str):
        return self.value == other

    @classmethod
    def validate(cls, value: str):
        phone_number = parse(value)

        if not is_valid_number(phone_number):
            raise ValueError(f'The phone is incorrect. The format should be {cls.PHONE_FORMAT_EXAMPLE}')

    @Field.value.setter
    def value(self, value: str):
        self.validate(value)
        self._Field__value = value
