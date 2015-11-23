# -*-coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.core.paginator import Paginator
from myblog.models import Articles, User, Admin
from myblog.logic.tools import *
from myblog.logic import user
import os, sys, time
import json
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.

def login(request):
	t = get_template("login.html")
	return HttpResponse(t.render())

def articleModify(request, articleId):

	loged = user.isLogin(request)
	if loged:
		t = get_template("add.html")
	else:
	 	t = get_template("login.html")

	article = Articles.objects.get(id=articleId)
	c = Context({
			"title": article.title,
			"content": article.content,
			"author": article.author,
			"articleId": articleId,
			"loged": loged,
			})
	return HttpResponse(t.render(c))

def addArticle(request):
	data = request.POST
	if data.has_key("articleId") and data["articleId"] != "":
		article = Articles.objects.get(id=data["articleId"])
		article.title = data["title"]
		article.author = data["author"]
		article.content = data["content"]
		article.tsp = time.strftime("%Y:%m:%d:%H:%M:%S")
	else:
		article = Articles(
			title = data["title"],
			author = data["author"],
			content = data["content"],
			tsp = time.strftime("%Y:%m:%d:%M:%S"),
			scanTimes = 0,
		)
	article.save()
	return HttpResponse(json.dumps({'CODE': 'ok'}));

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

def add(request):
	loged = user.isLogin(request)
	if loged:
		t = get_template("add.html")
	else:
	 	t = get_template("login.html")
	c = Context({
				"loged": loged,
			})
	return HttpResponse(t.render(c))

def getArticlePage(request):
	page = request.POST["page"]
	articles = Articles.objects.all()
	articles = sorted(articles, key=lambda article: -article.weight)
	p = Paginator(articles, 5)
	articles = p.page(page).object_list
	data = {
		"pageNum": p.num_pages,
		"articles": [],
	}

	t = get_template("markdown.html")
	global mon
	for item in articles:
		year, month, day, hour, minu, sec = item.tsp.split(":")
		tsp = mon[int(month) - 1] + " " + day + "/" + year
		data["articles"].append({
				"title": item.title,
				"tag": item.tag,
				"tsp": tsp,
				"desc": t.render({"data": item.content[0:100]+"\n\n..."}),
				"scanTimes": item.scanTimes,
				"articleId": item.id,
				})
	return HttpResponse(json.dumps(data))

def index(request):
	ip = getIP(request)
	t = get_template("index.html")
	c = Context({
			"title": "其实我只是个会计",
			"title2": "我们不生产代码, 我们只是代码的搬运工",
			"ip": ip,
			})
	html = t.render(c)
	response = HttpResponse(html)
	return response

def article(request, articleId):
	t = get_template("article.html")
	loged = user.isLogin(request)
	article = Articles.objects.get(id=articleId)
	article.scanTimes += 1
	article.save()
	global mon
	year, month, day, hour, minu, sec = article.tsp.split(":")
	tsp = mon[int(month) - 1] + " " + day + "/" + year
	return HttpResponse(t.render(Context({
					"articleId": article.id,
					"articleTitle": article.title,
					"content": article.content,
					"author": article.author,
					"scanTimes": article.scanTimes,
					"weight": article.weight,
					"tsp": tsp,
					"desc": article.desc,
					"tag": article.tag,
					"loged": loged,
					})))

def contact(request):
	t = get_template("contact.html")
	return HttpResponse(t.render(Context({
					"title": "其实我只是个会计",
					"title2": "我们不生产代码，我们只是代码的搬运工",
					})))
