from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReportList.as_view(), name='home'),
    path('about/', views.about_site, name='about'),
    path('create/', views.create_report, name='create'),
    path('like/<slug:slug>/', views.like_report, name='like_report'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('profile/<slug:author>/', views.user_profile, name='user_profile'),
    path('<slug:slug>/', views.full_report, name='full_report'),
    path('<slug:slug>/edit/', views.edit_report, name='edit_report'),
    path('<slug:slug>/delete/<int:report_id>/', views.delete_report, name='delete_report'),
]
