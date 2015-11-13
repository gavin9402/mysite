from markdown import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()
@register.filter(name="my_markdown")
def my_markdown(value):
	return markdown(value)
