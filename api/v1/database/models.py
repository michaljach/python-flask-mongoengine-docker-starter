from mongoengine import Document, StringField


class Todo(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
