from django import forms
from .models import Comment, Report



class CommentForm(forms.ModelForm):
    """
    Form for user to add comment.
    """
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            "content": "Enter your comment here:",
        }


class ReportForm(forms.ModelForm):
    """
    Form for user to add report.
    """
    class Meta:
        model = Report
        fields = ('title', 'content', 'status', 'featured_image')
        labels = {
            "title": "Report Title:",
            "content": "Enter your report here:",
            "status": "Is this a draft?",
            "featured_image": "Upload an image:",
        }