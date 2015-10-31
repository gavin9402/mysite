from django.conf.urls import include, url
from myblog.views import *
import settings

urlpatterns = [
	url(r"^$", index),
	url(r"^index/$", index)
]
