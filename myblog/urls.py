from django.conf.urls import include, url
from myblog.views import *
import settings

urlpatterns = [
	url(r"^$", index),
	url(r"^index/$", index),
	url(r"^article/(\d+)/$", article),
	url(r"^contact/$", contact),
	url(r"^admin/$", admin),
	url(r"^login/$", login),
	url(r"^loginSubmit/$", loginSubmit),
	url(r"^add/$", add),
	url(r"^addArticle/$", addArticle),
	url(r"^getArticlePage/$", getArticlePage),
]
