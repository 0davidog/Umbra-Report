from django import forms
from .models import Comment, Report


class CommentForm(forms.ModelForm):
    """
    Form for user to add comment.
    Related to :model: `Comment`
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
    Related to :model: `Report`
    """
    class Meta:
        model = Report
        fields = (
            'title', 'description', 'content', 'status', 'featured_image'
        )
        labels = {
            "title": "Report Title:",
            "description": "A brief description:",
            "content": "Enter your report here:",
            "status": "Choose Published or Draft:",
            "featured_image": "Upload an image:",
        }
