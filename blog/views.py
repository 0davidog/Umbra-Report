from django.shortcuts import render
from django.views import generic
from .models import Report

# Create your views here.

class ReportList(generic.ListView):
    queryset = Report.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6