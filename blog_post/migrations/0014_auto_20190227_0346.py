# Generated by Django 2.1.7 on 2019-02-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0013_auto_20190227_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.CharField(default='MXapbg8jYMM85-JZ3k1kW', editable=False, max_length=21, primary_key=True, serialize=False),
        ),
    ]
