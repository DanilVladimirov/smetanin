from django.db import models


class Publication(models.Model):
    TYPE = (
        ('achievement', 'досягнення'),
        ('publication', 'публікація')
    )
    img = models.ImageField()
    type = models.CharField(choices=TYPE, default='', max_length=100)
    title = models.CharField(max_length=200, default='')
    text = models.TextField(default='')

    def __str__(self):
        return self.title


class Contact(models.Model):
    pib = models.CharField(max_length=300, default='')
    mail = models.EmailField(default='')
    title = models.CharField(max_length=200, default='')
    text = models.TextField(default='')

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=100, default='')
    photo = models.ImageField()

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100, default='')
    img = models.ImageField(default='programmer.jpg')
    photos = models.ManyToManyField(Photo)

    def __str__(self):
        return self.title
