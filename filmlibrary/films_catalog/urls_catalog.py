from django.urls import path
from .views import main_menu, genre_list, film_detail, genre_detail, add_review

app_name = 'film'
urlpatterns = [
    path('', main_menu, name = 'main_menu'),
    path('genre/', genre_list, name = 'genre_list'),
    path('film/<int:pk>', film_detail, name='film_detail'),
    path('genre/<slug>', genre_detail, name='genre_detail'),
    path('film/<int:pk>/add_review', add_review, name = 'add_review'),
]