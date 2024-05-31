import django_filters


# from .models import ParentAuthor, ParentPost

class AuthorFilter(django_filters.FilterSet):
    class Meta:
        # model = ParentAuthor
        fields = ['name', 'biography', 'date_of_birth']


class PostFilter(django_filters.FilterSet):
    class Meta:
        # model = ParentPost
        fields = ['title', 'content', 'author', 'publication_date']
