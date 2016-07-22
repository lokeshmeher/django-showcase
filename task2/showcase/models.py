from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
	name = models.CharField(max_length=30)


class Product(models.Model):
	title = models.CharField(max_length=50)
	rating = models.PositiveIntegerField(default=0)
	description = models.TextField()
	tags = models.ManyToManyField(Tag)
