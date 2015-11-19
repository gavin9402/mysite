# -*-coding: utf-8 -*-
from myblog.logic.tools import *
from myblog.models import Admin, User
from django.http import HttpResponse
from myblog.conf import conf
import json

def adminLogin(data):
	mobile = data["mobile"]
	password = md5(data["password"])
	response = {}
	try:
		admin = Admin.objects.get(mobile=mobile)
		if password == admin.password:
			response = {
				"CODE":		"ok",
			}
		else:
			response = {
				"CODE":		"error",
				"errMsg":	"密码错误",
			}
	except Admin.DoesNotExist:
		response = {
			"CODE":		"error",
			"errMsg":	"用户不存在",
		}
	httpResponse = HttpResponse(json.dumps(response))
	if (response["CODE"] == "ok"):
		cookie = md5(mobile)
		httpResponse.set_cookie("cookie", cookie, conf("COOKIE_AGE"))
		admin.cookie = cookie
		admin.save()
	return httpResponse

def userLogin(data):
	mobile = data["mobile"]
	password = md5(data["password"])
	response = {}
	try:
		admin = User.objects.get(mobile=mobile)
		if password == admin.password:
			response = {
				"CODE":		"ok",
			}
		else:
			response = {
				"CODE":		"error",
				"errMsg":	"密码错误",
			}
	except User.DoesNotExist:
		response = {
			"CODE":		"error",
			"errMsg":	"用户不存在",
		}
	httpResponse = HttpResponse(json.dumps(response))
	if (response["CODE"] == "ok"):
		cookie = md5(mobile)
		httpResponse.set_cookie("cookie", cookie, conf("COOKIE_AGE"))
		admin.cookie = cookie
		admin.save()
	return httpResponse

def isLogin(request):
	if "cookie" not in request.COOKIES:
		return False
	return True

def userInfo(request):
	if isLogin(request) == False:
		return None
	cookie = request.COOKIES["cookie"]
	return User.objects.get(cookie=cookie)

def adminInfo(request):
	if isLogin(request) == False:
		return None
	cookie = request.COOKIES["cookie"]
	return Admin.objects.get(cookie=cookie)
