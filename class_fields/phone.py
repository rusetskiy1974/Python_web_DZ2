import re
from .field import Field


class Phone(Field):
    def __eq__(self, other: str):
        return self.value == other

    @staticmethod
    def validate(value):
        result = re.match(r'^\d{10}$', value)

        if result is None:
            print ('The phone must contain 10 digits')
            raise ValueError


    @Field.value.setter
    def value(self, value: str):
        self.validate(value)
        self._Field__value = value
