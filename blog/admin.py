from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Report, Comment, About


@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Comment)
admin.site.register(About)

