from django.contrib import admin

from .models import Image,Profile,Comment,Follow

# admin.site.register(Editor)


# Register your models here.

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)

