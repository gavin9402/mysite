# -*- coding: utf-8 -*-
import os, sys
reload(sys)
sys.setdefaultencoding('utf-8')

mon = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
monDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getArticleContent(fName):
	rootPath = sys.path[0]
	fp = open(rootPath+ "/myblog/articles/" + fName, "r")
	ret = ""
	for line in fp:
		ret += line
	return ret

def setCookies(cookies, response):
	for item in cookies:
		cookie = [
			"",
			"",
			None,
			None,
			"/",
			None,
			False,
		]
		n = len(item)
		for i in range(0, n):
			cookie[i] = item[i]
		response.set_cookie(cookie[0], cookie[1], cookie[2], cookie[3],
							cookie[4], cookie[5], cookie[6])
	return response

def md5(str):
	import hashlib
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

def getIP(request):
	if request.META.has_key('HTTP_X_FORWARDED_FOR'):
		ip =  request.META['HTTP_X_FORWARDED_FOR']
	else:
		ip = request.META['REMOTE_ADDR']
	return ip

def isLeap(year):
	return (year%400 == 0 or (year%100 != 0 and year%4 == 0))

if __name__ == "__main__":
	print 0+isLeap(2012)
	print 0+isLeap(2013)
