from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Report, Comment

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "blog/full_report.html",
        {"report": post,
        "comments": comments,
        "comment_count": comment_count,},
    )