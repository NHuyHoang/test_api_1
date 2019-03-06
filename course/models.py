from django.db import models
from nanoid import generate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    id = models.CharField(
        max_length=21, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.id:
            self.id = generate()
        super().save(*kwargs)

    def clean(self):
        if(self.date_start > self.date_end):
            raise ValidationError(_('Start date must bigger than end date'))

    def to_json(self):
        return dict(
            id=self.id,
            name=self.name,
            date_start=self.date_start,
            date_end=self.date_end
        )
