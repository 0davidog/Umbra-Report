from django import forms
from django.core.exceptions import ValidationError
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
            'title', 'description', 'category',
            'content', 'source', 'status', 'featured_image',
            'image_title', 'image_credit', 'image_source'
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

        """
        Custom clean method to check file size and type.
        Cloudinary expects:
        JPG, PNG, GIF, BMP, TIFF, ICO, PDF, EPS, PSD, SVG, WebP, JXR, and WDP.
        """

        def clean(self):
            # Call the parent class's clean method to get cleaned data
            cleaned_data = super().clean()

            # Retrieve the 'featured_image' from the cleaned data
            featured_image = cleaned_data.get('featured_image')

            # Initialize a list to store potential errors
            errors = []

            # Check if there is a featured_image uploaded
            if featured_image:
                # List of valid file extensions
                valid_file_extensions = [
                    'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff',
                    'ico', 'pdf', 'eps', 'psd', 'svg',
                    'webp', 'jxr', 'wdp'
                    ]

                # Extract the file extension from the file name
                ext = featured_image.name.split('.')[-1]

                # Check if the file is in the list of valid extensions
                if ext.lower() not in valid_file_extensions:
                    # Add an error if the file extension is not valid
                    self.add_error('featured_image', ValidationError(
                        'Unsupported image type.'))

                # Check if the file size is within the limit of 10MB
                if featured_image.size > 10485760:  # 10MB in bytes
                    # Add an error if the file size exceeds the limit
                    self.add_error('featured_image', ValidationError(
                        'Please submit a smaller image'
                        ))

            # Return the cleaned data
            return cleaned_data
