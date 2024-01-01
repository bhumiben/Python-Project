from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    title = models.CharField(max_length=200)
    book_id = models.IntegerField()
    author = models.CharField(max_length=100)
    publishedby_year = models.IntegerField()
    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
