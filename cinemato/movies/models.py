from django.db import models

class genre(models.Model):
    name = models.CharField(max_length=20)

class actor(models.Model):
    last_name  = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)

class director(models.Model):
    last_name  = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)

class producer(models.Model):
    last_name  = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)

class technician(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

class movie(models.Model):
    name         = models.CharField(max_length=30)
    rating       = models.FloatField()
    genres       = models.ManyToManyField(genre,related_name='movies')
    actors       = models.ManyToManyField(actor,related_name='movies')
    directors    = models.ManyToManyField(director,related_name='movies')
    producers    = models.ManyToManyField(producer,related_name='movies')
    technicians  = models.ManyToManyField(technician,related_name='movies')
    release_date = models.DateField()