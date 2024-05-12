from django import template
import products.views as views

register = template.Library()
@register.simple_tag()
def get_cats():
    return views.categories_db
@register.inclusion_tag('products/list_categories.html')
def show_categories():
    nav = views.categories_db
    return {"nav": nav}