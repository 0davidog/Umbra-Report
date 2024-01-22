from django.contrib import admin
from .models import Report, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Comment)