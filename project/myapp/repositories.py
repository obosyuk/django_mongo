import os
from .models.sqlite import Author as SQLiteAuthor, Post as SQLPost
from .models.mongo import Author as MongoAuthor, Post as MongoPost


def get_concrete_models():
    db_type = os.environ.get('DATABASE_TYPE', 'mongo')
    if db_type == 'sqlite':
        return SQLiteAuthor, SQLPost
    elif db_type == 'mongo':
        return MongoAuthor, MongoPost
    else:
        raise ValueError("Invalid database type specified in DATABASE_TYPE environment variable")


Author, Post = get_concrete_models()


class AuthorRepository:
    def get_authors(self):
        return Author.objects.all()

    def create_author(self, **kwargs):
        return Author.objects.create(**kwargs)

    def update_author(self, id, **kwargs):
        author = Author.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(author, key, value)
        author.save()
        return author

    def delete_author(self, id):
        author = Author.objects.get(id=id)
        author.delete()


class PostRepository:
    def get_posts(self):
        return Post.objects.all()

    def create_post(self, **kwargs):
        return Post.objects.create(**kwargs)

    def update_post(self, id, **kwargs):
        post = Post.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(post, key, value)
        post.save()
        return post

    def delete_post(self, id):
        post = Post.objects.get(id=id)
        post.delete()
