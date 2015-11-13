# -*-coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from myblog.models import Articles, User, Admin
from myblog.logic.tools import *
from myblog.logic import user
import os, sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.

def login(request):
	t = get_template("login.html")
	return HttpResponse(t.render())

def loginSubmit(request):
	data = request.POST
	mobile = data["mobile"]
	password = md5(data["password"])
	loginType = data["type"]
	if loginType == "admin":
		return user.adminLogin(data)
	elif loginType == "user":
		return user.userLogin(data)

def admin(request):
	return ""

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
				"articleId": item.id,
				})
	c = Context({
			"title": "其实我只是个会计",
			"title2": "我们不生产代码, 我们只是代码的搬运工",
			"articles": articles,
			"page": 1,
			"pageTotal": 1,
			})
	html = t.render(c)
	response = HttpResponse(html)
	return response

def article(request, articleId):
	t = get_template("article.html")
	fName = "markdown.blog"
	return HttpResponse(t.render(Context({
					"articleId": articleId,
					"articleTitle": "Django Markdown",
					"content": getArticleContent(fName),
					})))

def contact(request):
	t = get_template("contact.html")
	return HttpResponse(t.render(Context({
					"title": "其实我只是个会计",
					"title2": "我们不生产代码，我们只是代码的搬运工",
					})))
