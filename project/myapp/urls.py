from django.urls import path
from .views import AuthorListCreateView, AuthorRetrieveUpdateDestroyView, PostListCreateView, \
    PostRetrieveUpdateDestroyView, AuthorListCreateAPIView

urlpatterns = [
    # path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),

]
