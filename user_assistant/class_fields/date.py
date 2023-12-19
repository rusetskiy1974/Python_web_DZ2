from datetime import datetime
import re

from .field import Field


class Date(Field):
    DATE_FORMAT = '%d.%m.%Y'

    def __str__(self):
        return self.value.strftime(self.DATE_FORMAT)

    @staticmethod
    def validate(value: str):
        result = re.match(r'\d{2}\.\d{2}\.\d{4}', value)

        if result is None:
            raise ValueError('The date is incorrect')


    @Field.value.setter
    def value(self, value: str):
        self.validate(value)
        self._Field__value = datetime.strptime(value, self.DATE_FORMAT).date()
