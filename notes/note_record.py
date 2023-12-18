from class_fields.name import Name


class NoteRecord():
    def __init__(self, name: Name, record: str):
        self.name = name
        self.record = record

    def add_teg(self, teg):
        self.teg = teg    

    def __str__(self):
        return f"Title : {self.name.value}, record: {self.record}"

    def __repr__(self):
        return f"Title : {self.name.value}, record: {self.record}" 


         