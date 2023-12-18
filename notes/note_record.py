import datetime


class NoteRecord:
    def __init__(self, author, text, tags, date=None):
        self.author = author
        self.text = text
        self.tags = tags
        self.date = date if date else datetime.datetime.now()

    # зміна тексту нотатки
    def update_text(self, new_text):
        self.text = new_text

    # зміна автора
    def update_author(self, new_author):
            self.author = new_author

    # зміна тегу
    def update_tags(self, new_tags):
        self.tags = new_tags


         