from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ["created_at", "updated_at", "posted_by"]
