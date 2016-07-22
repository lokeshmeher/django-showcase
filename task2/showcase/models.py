from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	tags = models.ManyToManyField()
