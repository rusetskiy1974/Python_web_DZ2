from .field import Field


class Address(Field):
    @staticmethod
    def validate(value):
        if not value:
            print ('The adress is required')
            raise ValueError

    @Field.value.setter
    def value(self, value: str):
        self.validate(value)
        self._Field__value = value