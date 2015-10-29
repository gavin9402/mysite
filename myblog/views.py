from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

def index(request):
	t = get_template("index.html")
	return HttpResponse(t.render())
