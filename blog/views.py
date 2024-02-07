from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Report, Comment, User, About
from .forms import CommentForm, ReportForm

# Create your views here.

class ReportList(generic.ListView):
    queryset = Report.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def full_report(request, slug):

    queryset = Report.objects.filter(status=1)
    report = get_object_or_404(queryset, slug=slug)

    comments = report.comments.all().order_by("-created_on")
    comment_count = report.comments.filter(approved=True).count()
    comment_form = CommentForm()

    liked = False
    if report.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = report
        comment.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval')
        comment_form = CommentForm()


    return render(
        request,
        "blog/full_report.html",
        {"report": report,
         "liked": liked,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,},
    )

def edit_comment(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

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
            comment_form = CommentForm()
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
            comment_form = CommentForm()

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
    if request.method == "POST":
        report_form = ReportForm(request.POST, request.FILES)
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.author = request.user
            report.featured_image = request.FILES.get('featured_image')
            report.save()
            messages.success(request, 'Report submitted and awaiting approval')
            return redirect('home')
        
        else:
            messages.error(request, 'Error submitting the report. Please check the form.')

    else:
        report_form = ReportForm()

    return render(request, "blog/create_report.html", {
        "report_form": report_form,
        },
        )

def like_report(request, slug):
    
    post = get_object_or_404(Report, slug=slug)
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('full_report', args=[slug]))

def about_site(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "blog/about.html",
        {"about": about},
    )

def user_profile(request, author):
    
    username = User.objects.filter(username=author)
    profile = get_object_or_404(username, username=author)
    report_list = Report.objects.filter(author=profile)

    return render(
        request, "blog/user_profile.html", {
        "username": username,
        "report_list": report_list,
        },
        )
