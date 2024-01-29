from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Report, Comment
from .forms import CommentForm, ReportForm

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

def edit_comment(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        print('post')

        queryset = Report.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('full_report', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Report.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('full_report', args=[slug]))


def create_report(request):

    report_form = ReportForm()

    if request.method == "POST":
        report_form = ReportForm(data=request.POST)
    if report_form.is_valid():
        report = report_form.save(commit=False)
        report.author = request.user
        report.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Report submitted and awaiting approval'
    )

    return render(request, "blog/create_report.html",
        {"report_form": report_form,},
    )