from mongoengine import Document, StringField, DateField, ReferenceField, CASCADE


class Author(Document):
    name = StringField(max_length=100, required=True)
    biography = StringField(required=True)
    date_of_birth = DateField(required=True)


class Post(Document):
    title = StringField(max_length=100, required=True)
    content = StringField(required=True)
    author = ReferenceField('Author', reverse_delete_rule=CASCADE)
    publication_date = DateField(required=True)
