# Generated by Django 2.1.7 on 2019-02-27 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0011_auto_20190227_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.CharField(default='rn5OzJFeaJZPejuPfb7d6', editable=False, max_length=21, primary_key=True, serialize=False),
        ),
    ]
