# Generated by Django 2.1.7 on 2019-02-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190227_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='register', to='course.Course'),
        ),
    ]
