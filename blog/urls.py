from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReportList.as_view(), name='home'),
    path('<slug:slug>/', views.full_report, name='full_report'),
]