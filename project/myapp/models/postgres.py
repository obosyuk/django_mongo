from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
