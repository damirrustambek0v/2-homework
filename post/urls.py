
from django.urls import path
from .views import (
    PostListCreateView, PostDetailAPIView,
    CategoryListCreateView, CommentListCreateView,
    CommentAPIView, TagListCreateView )


app_name = 'post'

urlpatterns = [
        path('categories/', CategoryListCreateView.as_view(), name='categories'),
        path('comments/', CommentListCreateView.as_view(), name='comments'),
        path('comments/<int:pk>/', CommentAPIView.as_view(), name='post-comments'),
        path('posts/', PostListCreateView.as_view(), name='post'),
        path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
        path('tags/', TagListCreateView.as_view(), name='tags'),
]
