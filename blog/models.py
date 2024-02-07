from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Report(models.Model):
    class Meta:
        ordering = ["-updated_on"]
    title = models.CharField(max_length=250, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', editable=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    # One user can write many posts, so this is a one-to-many or Foreign Key. The cascade on delete means that on the deletion of the user entry, all their posts are also deleted.
    featured_image = CloudinaryField('Featured Image', default='placeholder')
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def likes_number(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment: {self.content} by {self.author}"
    

class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
