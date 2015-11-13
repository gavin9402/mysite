from django.db import models

class Articles(models.Model):
	title = models.CharField(max_length=20)
	tag = models.CharField(max_length=10)
	tsp = models.CharField(max_length=10)
	desc = models.CharField(max_length=255)
	content = models.TextField()
	scanTimes = models.IntegerField()

class User(models.Model):
	mobile = models.CharField(max_length = 13)
	password = models.CharField(max_length = 13)
	email = models.CharField(max_length = 22)
	name = models.CharField(max_length = 22)
	cookie = models.CharField(max_length = 255)

class Admin(models.Model):
	mobile = models.CharField(max_length = 13)
	password = models.CharField(max_length = 13)
	email = models.CharField(max_length = 22)
	name = models.CharField(max_length = 22)
	cookie = models.CharField(max_length = 255)
