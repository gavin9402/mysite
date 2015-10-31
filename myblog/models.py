from django.db import models

class Articles(models.Model):
	title = models.CharField(max_length=20)
	tag = models.CharField(max_length=10)
	tsp = models.CharField(max_length=10)
	desc = models.CharField(max_length=255)
	content = models.TextField()
