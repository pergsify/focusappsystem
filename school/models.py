from __future__ import unicode_literals

from django.db import models

class Teacher(models.Model):
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	middleName = models.CharField(max_length=200)
	emailAddress = models.EmailField()
