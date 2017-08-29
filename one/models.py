from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length = 255, blank = False)

	def __str__(self):
		return self.name


class Employee(models.Model):
	name = models.CharField(max_length = 255, blank = False)
	dept = models.ForeignKey(Department)

	def __str__(self):
		return self.name + " -->> " + self.dept.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()

