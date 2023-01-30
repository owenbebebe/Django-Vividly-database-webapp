from django.urls import path
from . import views

app_name = 'movies'

# mapping this to a view function
urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='detail')
]
