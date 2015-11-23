from django.core.management.base import BaseCommand,CommandError     
from myblog.models import Articles, User, Admin
from myblog.logic.tools import *

def calWeight(article):
	y1 = 2015
	m1 = 11
	d1 = 18
	y2, m2, d2 = article.tsp.split(":")[0:3]
	y2 = int(y2)
	m2 = int(m2)
	d2 = int(d2)
	ret = -322
	for year in range(y1, y2):
		ret += 365 + isLeap(year)
	global mon, monDays
	for month in range(0, m2-1):
		ret += monDays[month]
	return ret + d2 + article.scanTimes
	
class Command(BaseCommand):
	def handle(self, *arg, **args):
		articles = Articles.objects.all()
		for article in articles:
			article.weight = calWeight(article)
			article.save()
