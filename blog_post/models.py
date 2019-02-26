from django.db import models
from nanoid import generate


class BlogPost(models.Model):
    id = models.CharField(max_length=21, primary_key=True, default=generate(), editable=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
