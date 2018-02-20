from markdownx.utils import markdownify
from django import template

register = template.Library()


@register.filter
def formatted_markdown(text):
    return markdownify(text)
