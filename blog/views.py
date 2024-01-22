from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Report

# Create your views here.

class ReportList(generic.ListView):
    queryset = Report.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def full_report(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/full_report.html`
    """

    queryset = Report.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/full_report.html",
        {"report": post},
    )