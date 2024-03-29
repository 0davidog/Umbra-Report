from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Report(models.Model):
    """
    Represents a report with a title, content, author, status,
    and other related fields.

    Related to :model: `auth.User`

    Attributes:
        title (str):
        The title of the report, limited to 250 characters.
        slug (str):
        The slugified version of the title,
        used for generating SEO-friendly URLs.
        author (User):
        The user who authored the report.
        category (str):
        A choice of 4 categories to label the report.
        source (str):
        The URL of the story source.
        featured_image (str):
        The URL of the featured image for the report.
        image_title (str):
        Title of the featured_image
        image_credit (str):
        Author of the featured_image
        image_source:
        URL source of the featured_image.
        content (str):
        The main content/body of the report.
        description (str):
        A brief description or summary of the report content.
        status (int):
        The status of the report, chosen from predefined choices.
        created_on (datetime):
        The date and time when the report was created.
        updated_on (datetime):
        The date and time when the report was last updated.
        approved (boolean):
        Indicates whether the report is approved or not.
        likes (ManyToManyField):
        The users who have liked the report.

    Methods:
        __str__():
        Returns a string representation of the report,
        consisting of the title and author.
        likes_number():
        Returns the number of likes the report has received.
    """

    class Meta:
        ordering = ["-updated_on"]
    title = models.CharField(max_length=250, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', editable=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    # One user can write many posts, so this is a one-to-many or Foreign Key.
    # The cascade on delete means that on the deletion of the user entry,
    # all their posts are also deleted.
    CATEGORY_CHOICES = [
        ("1", "True Story"),
        ("2", "Urban Legend"),
        ("3", "Creative Writing"),
        ("4", "Creepypasta"),
    ]
    category = models.CharField(
        max_length=250, default="3", null=False, choices=CATEGORY_CHOICES
    )
    source = models.URLField(
        max_length=200, blank=True
    )
    featured_image = CloudinaryField(
        'Featured Image',
        default='placeholder'
    )
    image_title = models.CharField(max_length=250, blank=True)
    image_credit = models.CharField(max_length=250, blank=True)
    image_source = models.URLField(max_length=200, blank=True)
    content = models.TextField()
    description = models.CharField(max_length=500, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User,
        related_name='blogpost_like',
        blank=True
    )

    def __str__(self):
        return f'{self.title} by {self.author}'

    def likes_number(self):
        """
        Returns the number of likes the report has received.

        Returns:
            int: The number of likes for the report.
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Adapted from Code Institute Walkthough Project.
    Represents a comment on a report.
    Related to :model: `auth.User`
    Related to :model: `Report`

    Attributes:
        post (Report):
        The report to which the comment is associated.
        content (str):
        The content/body of the comment.
        author (User):
        The user who authored the comment.
        approved (boolean):
        Indicates whether the comment is approved or not.
        created_on (datetime):
        The date and time when the comment was created.
        updated_on (datetime):
        The date and time when the comment was last updated.

    Methods:
        __str__():
        Returns a string representation of the comment,
        consisting of the content and author.
    """

    post = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the comment,
        consisting of the content and author.

        Returns:
            str: A string representation of the comment.
        """
        return f"Comment: {self.content} by {self.author}"


class About(models.Model):
    """
    Adapted from Code Institute Walkthough Project.
    Represents information about the site.

    Attributes:
        title (str):
        The title or heading of the about section, limited to 200 characters.
        updated_on (datetime):
        The date and time when the about section was last updated.
        content (str):
        The content or description of the about section.

    Methods:
        __str__():
        Returns a string representation of the about section,
        consisting of the article title.
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the about section,
        consisting of the title.

        Returns:
            str: A string representation of the about section.
        """
        return self.title
