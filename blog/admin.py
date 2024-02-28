from django.contrib import admin
from .models import Report, Comment, About

# Register your models here.
admin.site.register(Report)
admin.site.register(Comment)
admin.site.register(About)
