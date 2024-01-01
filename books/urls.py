from django.urls import path, include

from .views import *

urlpatterns = [
    path("", books, name="books"),
    path("book/<str:pk>/", book, name="book"),
    path("add_book", addBook, name="add_book"),
    path("update_book/<int:pk>", updateBook, name="update_book"),
    path("delete_movie/<int:pk>", deleteBook, name="delete_book"),
    path("login", loginPage, name="login"),
    path("logout", logoutUser, name="logout"),
    path("register", registerUser, name="register"),
    path("api/", include("books.api.urls")),
]
