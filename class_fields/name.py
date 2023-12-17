from .field import Field


class Name(Field):
    @staticmethod
    def validate(value):
        if not value:
            print ('The name is required')
            raise ValueError

    @Field.value.setter
    def value(self, value: str):
        self.validate(value)
        self._Field__value = value


name = Name('Alex')
