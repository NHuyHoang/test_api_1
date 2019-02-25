from django.db import models


class Post(models.Model):
    userId = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    body = models.CharField(max_length=256)

    def __str__(self):
        return self.body
