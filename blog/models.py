from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError



def validate_video_duration(file):
    from moviepy.editor import VideoFileClip
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(delete=False, suffix='.mp4') as temp:
        temp.write(file.read())
        file.seek(0)  # reset pointer
        video = VideoFileClip(temp.name)
        if video.duration > 60:
            raise ValidationError("Video must be 60 seconds or less.")
        video.close()




class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, allow_unicode=True, unique=True)


    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    video = models.FileField(upload_to='post_videos/', null=True, blank=True, validators=[validate_video_duration])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.image and self.video:
            raise ValidationError("You can upload either an image or a video, not both.")
            
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username}'