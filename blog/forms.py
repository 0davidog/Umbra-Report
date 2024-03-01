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
            'title', 'description', 'category', 'content', 'source', 'status', 'featured_image', 'image_title', 'image_credit', 'image_source'
        )
        labels = {
            "title": "Report Title:",
            "description": "A brief description:",
            "category": "Choose a category:",
            "content": "Enter your report here:",
            "source": "Add a link to a source or inspiration:",
            "status": "Choose Published or Draft:",
            "featured_image": "Upload an image:",
            "image_title": "Does the image have a title?",
            "image_credit": "Do you know who made this image?",
            "image_source": "Did this image come from somewhere else?",
        }
