import datetime


class NoteRecord:
    def __init__(self, author, text, tags, date=None):
        self.author = author
        self.text = text
        self.tags = tags
        self.date = date if date else datetime.datetime.now()

    def update_text(self, new_text):
        self.text = new_text

    def update_author(self, new_author):
            self.author = new_author

    def update_tags(self, new_tags):
        self.tags = new_tags


         