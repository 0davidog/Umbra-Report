from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Report, Comment
from .forms import CommentForm

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
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

    return render(
        request,
        "blog/full_report.html",
        {"report": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,},
    )