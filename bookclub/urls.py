from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name="all_books"),
    path('book-list', views.book_list, name="book_list"),
    path('book/<int:pk>/', views.book_detail, name="book_detail"),

]