from django import template
from examWeb.web.models import Profile

register = template.Library()


@register.simple_tag()
def user_profile():
    result = Profile.objects.all()
    if result:
        return True
    return False
