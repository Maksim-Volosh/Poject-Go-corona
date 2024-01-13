from django import template
import main.views as views

register = template.Library()


@register.simple_tag()
def get_names():
    pass

@register.inclusion_tag("main/")
def show_category():
    pass