from __future__ import unicode_literals

from django.db import models

import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Teacher(models.Model):
	first_Name = models.CharField(max_length=200)
	last_Name = models.CharField(max_length=200)
	middleName = models.CharField(max_length=200)
	emailAddress = models.EmailField()

class SchoolYear(models.Model):
	#start_Year = models.DateField()
	start_Year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)


class Faculty(models.Model):
	name = models.CharField(max_length=200)
	