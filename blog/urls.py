from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReportList.as_view(), name='home'),
]