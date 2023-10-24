from django.contrib import admin
from base.models import (
    UserProfile,
    Blog,
    Comment,
    Likes,
)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)
