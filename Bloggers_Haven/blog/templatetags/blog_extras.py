from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def get_profile_image(username):
    try:
        user = User.objects.get(username=username)
        return user.profile.image.url
    except User.DoesNotExist:
        return 'default.jpg'