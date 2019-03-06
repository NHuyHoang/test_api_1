from django.db import models
from nanoid import generate
from course.models import Course


class Student(models.Model):
    id = models.CharField(max_length=21, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='register')

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.id:
            self.id = generate()
        super().save(*kwargs)

    def to_json(self):
        return dict(
            id=self.id,
            name=self.name
        )
