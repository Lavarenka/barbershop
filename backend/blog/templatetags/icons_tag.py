from django import template
from blog.models import SocialItem

register = template.Library()


@register.inclusion_tag("social_icons.html")
def get_social_icons():
    """all icons for footer"""
    icons = SocialItem.objects.all()
    return {"icons": icons}
