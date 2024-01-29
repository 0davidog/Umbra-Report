from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReportList.as_view(), name='home'),
    path('create/', views.create_report, name='create'),
    path('<slug:slug>/', views.full_report, name='full_report'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]