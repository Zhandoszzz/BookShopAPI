from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    authors = models.ManyToManyField('Author')
    description = models.TextField()
    cover = models.ImageField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField('Book')
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
