from django.http import HttpResponse
from django import template
from django.template.loader import get_template
import json

def index(request):
	t = get_template("index.html")
	return HttpResponse(t.render())
