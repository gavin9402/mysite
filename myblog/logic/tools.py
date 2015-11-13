# -*- coding: utf-8 -*-
import os, sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
