# Generated by Django 2.1.7 on 2019-02-27 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.CharField(default='PPgQ41u7BjOmbAer1zG2B', editable=False, max_length=21, primary_key=True, serialize=False),
        ),
    ]
