from django.db import models

# Create your models here.

class post(models.Model):
	author = models.CharField(max_length=40)
	time_posted = models.DateTimeField('Time Posted')
	post = models.CharField(max_length=1000)

	