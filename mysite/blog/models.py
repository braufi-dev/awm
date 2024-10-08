from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# Custom manager to retrieve all posts that have a PUBLISHED status
class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)

# The Post model for blog posts
class Post(models.Model):

    # Adding a status fields to store the posts either as drafts or a published
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()

    # Create a relationship between users model already available on django and posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")

    # Adding date-time eleemnts to the posts, data of creation, publication and update
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Adding status here as table fields through ORM
    status = models.CharField(max_length=2, 
                              choices=Status.choices, 
                              default=Status.DRAFT
    )

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self) -> str:
        return super().__str__()
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', 
                       args=[
                           self.publish.year,
                           self.publish.month,
                           self.publish.day,
                           self.slug
                       ])
