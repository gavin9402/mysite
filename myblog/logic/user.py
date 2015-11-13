# -*-coding: utf-8 -*-
from myblog.logic.tools import *
from myblog.models import Admin, User
from django.http import HttpResponse
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
	return HttpResponse(json.dumps(response))

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
	return HttpResponse(json.dumps(response))
