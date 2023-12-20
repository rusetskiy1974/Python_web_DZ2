from .field import Field
from datetime import datetime


class ID(Field):
    def __init__(self, init_id=datetime.timestamp(datetime.now())):
        super().__init__(init_id)