from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return '-'.join(self.name.lower().split())


@python_2_unicode_compatible
class Product(models.Model):
	title = models.CharField(max_length=50)
	rating = models.PositiveIntegerField(default=0)
	description = models.TextField()
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title
