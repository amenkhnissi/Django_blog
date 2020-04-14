from django.contrib import admin
from .models import post , Comment , Category

admin.site.register(post)
admin.site.register(Comment)
admin.site.register(Category)

