from django.contrib import admin
from .models import Report, Comment, About

# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on', 'approved', 'status']
    list_filter = ['status', 'approved', 'author']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author', 'created_on', 'approved', 'post']
    list_filter = ['approved', 'author', 'post']

admin.site.register(Report, ReportAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(About)
