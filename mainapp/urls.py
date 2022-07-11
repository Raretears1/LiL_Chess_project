from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('shop/', views.book_page, name='book_page'),
    path('players/', views.players_page, name='players_page'),
    path('debuts/', views.debuts_page, name='debuts_page'),
]
