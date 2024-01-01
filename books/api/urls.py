from django.urls import path
from .views import getRoutes, getBooks, getBook

urlpatterns = [
    path("api/", getRoutes, name="api_routes"),
    path("api/books/", getBooks, name="api_books"),
    path("api/books/<str:pk>/", getBook, name="api_book"),
]
