from .serializer import Serializer
from datetime import datetime, date
from class_fields.date import Date

class DateSerializer(Serializer):
    @staticmethod
    def serialize(value: date):
        return value.strftime(Date.DATE_FORMAT)

    @staticmethod
    def deserialize(value: str):
        return datetime.strptime(value, Date.DATE_FORMAT).date()