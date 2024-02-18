from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Report, Comment, User, About
from .forms import CommentForm, ReportForm

# Create your views here.

class ReportList(generic.ListView):
    """
    View for displaying a list of reports.

    Attributes:
        queryset (QuerySet): The queryset of reports to be displayed, filtered by status=1 (active).
        template_name (str): The name of the template used to render the list of reports.
        paginate_by (int): The number of reports to display per page, pagination is enabled.

    Note:
        This view inherits from Django's generic ListView class, which simplifies the implementation
        of views for displaying lists of objects.

    """
    queryset = Report.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def full_report(request, slug):
    """
    View for displaying the full details of a report and handling comments.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the report to be displayed.

    Returns:
        HttpResponse: The HTTP response containing the rendered full_report.html template with report details and comments.

    """
    # Retrieve the report object based on the provided slug, or return a 404 error if not found
    queryset = Report.objects.filter(status=1)
    report = get_object_or_404(queryset, slug=slug)
    
    # Retrieve all comments associated with the report, ordered by creation date
    comments = report.comments.all().order_by("-created_on")
    
    # Count the number of approved comments for the report
    comment_count = report.comments.filter(approved=True).count()
    
    # Initialize an empty comment form
    comment_form = CommentForm()
    
    # Check if the current user has already liked the report
    liked = False
    if request.user.is_authenticated:
        if report.likes.filter(id=request.user.id).exists():
            liked = True
    
    # If the request method is POST, process the comment form data
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        # If the comment form is valid, save the comment and display a success message
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = report
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            # Reset the comment form to display an empty form after submission
            comment_form = CommentForm()
    
    # Render the full_report.html template with the report details, comments, and comment form
    return render(
        request,
        "blog/full_report.html",
        {
            "report": report,
            "liked": liked,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def edit_comment(request, slug, comment_id):
    """
    View for editing comments.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the report associated with the comment.
        comment_id (int): The ID of the comment to be edited.

    Returns:
        HttpResponseRedirect: Redirects to the full_report view after processing the comment update.

    """
    # If the request method is POST, process the form submission
    if request.method == "POST":
        # Retrieve the report object based on the provided slug, or return a 404 error if not found
        queryset = Report.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        
        # Retrieve the comment object based on the provided comment_id, or return a 404 error if not found
        comment = get_object_or_404(Comment, pk=comment_id)
        
        # Create a comment form instance with the submitted data and the existing comment instance
        comment_form = CommentForm(data=request.POST, instance=comment)
        
        # Check if the comment form is valid and if the current user is the author of the comment
        if comment_form.is_valid() and comment.author == request.user:
            # Save the updated comment information
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Set approved to False after edit
            comment.save()
            # Display a success message
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            # Reset the comment form to display an empty form
            comment_form = CommentForm()
        else:
            # Display an error message if the comment form is invalid or the user is not the author of the comment
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
            # Reset the comment form to display an empty form
            comment_form = CommentForm()

    # Redirect to the full_report view after processing the comment update
    return HttpResponseRedirect(reverse('full_report', args=[slug]))
    

def comment_delete(request, slug, comment_id):
    """
    View for deleting a comment.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the report associated with the comment.
        comment_id (int): The ID of the comment to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the full_report view after processing the comment deletion.

    """
    # Retrieve the report object based on the provided slug, or return a 404 error if not found
    queryset = Report.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    
    # Retrieve the comment object based on the provided comment_id, or return a 404 error if not found
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the current user is the author of the comment
    if comment.author == request.user:
        # If so, delete the comment
        comment.delete()
        # Display a success message
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        # If not, display an error message
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    # Redirect to the full_report view after processing the comment deletion
    return HttpResponseRedirect(reverse('full_report', args=[slug]))


def create_report(request):
    """
    View for creating a new report.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered create_report.html template with the report form.

    """
    # If the request method is POST, process the form submission
    if request.method == "POST":
        # Create a report form instance with the submitted data and files
        report_form = ReportForm(request.POST, request.FILES)
        # If the report form is valid, save the report and display a success message
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.author = request.user
            report.featured_image = request.FILES.get('featured_image')
            report.save()
            messages.success(request, 'Report submitted and awaiting approval')
            return redirect('home')  # Redirect to the home page after successful submission
        else:
            # If the report form is invalid, display an error message
            messages.error(request, 'Error submitting the report. Please check the form.')

    else:
        # If the request method is not POST, create an empty report form instance
        report_form = ReportForm()

    # Render the create_report.html template with the report form
    return render(request, "blog/create_report.html", {"report_form": report_form})

def like_report(request, slug):
    
    post = get_object_or_404(Report, slug=slug)
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('full_report', args=[slug]))


def edit_report(request, slug):
    """
    View for editing an existing report.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the report to be edited.

    Returns:
        HttpResponse: The HTTP response containing the rendered edit_report.html template with the report form.

    """
    # Retrieve the report object based on the provided slug, or return a 404 error if not found
    edit = get_object_or_404(Report, slug=slug)

    # If the request method is POST, process the form submission
    if request.method == "POST":
        # Create a report form instance with the submitted data, files, and the instance of the report being edited
        report_form = ReportForm(request.POST, request.FILES, instance=edit)
        # If the report form is valid, save the updated report and display a success message
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.author = request.user
            report.featured_image = request.FILES.get('featured_image')
            report.save()
            messages.success(request, 'Report submitted and awaiting approval')
            return redirect('home')  # Redirect to the home page after successful submission
        else:
            # If the report form is invalid, display an error message
            messages.error(request, 'Error submitting the report. Please check the form.')

    else:
        # If the request method is not POST, create a report form instance with the instance of the report being edited
        report_form = ReportForm(instance=edit)

    # Render the edit_report.html template with the report form
    return render(request, "blog/edit_report.html", {"report_form": report_form})


def delete_report(request, slug, report_id):
    """
    View for deleting a report.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the report to be deleted.
        report_id (int): The ID of the report to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the home page after processing the report deletion.

    """
    # Retrieve the report object based on the provided slug and report ID, or return a 404 error if not found
    report = get_object_or_404(Report, slug=slug, pk=report_id)

    # Check if the current user is the author of the report
    if report.author == request.user:
        # If so, delete the report
        report.delete()
        # Display a success message
        messages.success(request, 'Report deleted successfully.')
        return redirect('home')  # Redirect to the home page after successful deletion
    else:
        # If not, display an error message
        messages.add_message(request, messages.ERROR, 'You can only delete your own reports!')
        # Redirect to the home page
        return HttpResponseRedirect(reverse('home'))


def about_site(request):
    """
    View for rendering the About page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered about.html template with the about object.

    """
    # Retrieve the latest about object
    about = About.objects.all().order_by('-updated_on').first()

    # Render the about.html template with the about object
    return render(
        request,
        "blog/about.html",
        {"about": about},
    )


def user_profile(request, author):
    """
    View for rendering a user's profile page.

    Args:
        request (HttpRequest): The HTTP request object.
        author (str): The username of the user whose profile is being viewed.

    Returns:
        HttpResponse: The HTTP response containing the rendered user_profile.html template with user profile information.

    """
    # Retrieve the user object based on the provided username
    username = User.objects.filter(username=author)
    # Retrieve the profile object for the user
    profile = get_object_or_404(username, username=author)
    # Retrieve the list of reports authored by the user
    report_list = Report.objects.filter(author=profile)

    # Render the user_profile.html template with the user profile information
    return render(
        request, "blog/user_profile.html", {
        "username": username,
        "report_list": report_list,
        },
        )


class Page404(TemplateView):
    template_name = '404.html'