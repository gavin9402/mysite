# -*-coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from myblog.models import Articles
# Create your views here.

def index(request):
	mon = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
	t = get_template("index.html")
	itemList = Articles.objects.all()
	articles = []
	for item in itemList:
		year = item.tsp[0: 4]
		month = item.tsp[4: 6]
		day = item.tsp[6:]
		tsp = mon[int(month) - 1] + " " + day + "/" + year
		articles.append({
				"title": item.title,
				"tag": item.tag,
				"tsp": tsp,
				"desc": item.desc,
				"scanTimes": item.scanTimes,
				})
	c = Context({
			"title": "其实我只是个会计",
			"title2": "我们不生产代码, 我们只是代码的搬运工",
			"articles": articles,
			"page": 1,
			"pageTotal": 1,
			})
	return HttpResponse(t.render(c))
