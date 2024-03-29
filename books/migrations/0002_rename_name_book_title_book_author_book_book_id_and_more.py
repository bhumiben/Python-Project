# Generated by Django 4.0 on 2023-12-13 04:10

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=datetime.datetime(2023, 12, 12, 23, 8, 50, 879302), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publishedby_year',
            field=models.IntegerField(default=1975),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.PositiveIntegerField(default=1975, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
