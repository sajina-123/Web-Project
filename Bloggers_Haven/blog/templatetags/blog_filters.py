from django import template
from django.conf import settings

register = template.Library()

@register.filter
def get_profile_image(user):
    try:
        if user.profile.image:
            return user.profile.image.url
        else:
            return f"{settings.MEDIA_URL}profile_pics/default.jpg"
    except Exception:
        return f"{settings.MEDIA_URL}profile_pics/default.jpg"