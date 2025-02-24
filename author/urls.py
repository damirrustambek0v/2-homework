from django.urls import path
from .views import AuthorListCreateView


app_name = 'author'

urlpatterns = [
    path('api/create/', AuthorListCreateView.as_view(), name='create'),

]
