# -*- coding: utf-8 -*-

dict = {
	"COOKIE_AGE": 7 * 24 * 3600,
}

def conf(key):
	if key not in dict:
		return None
	return dict[key]
