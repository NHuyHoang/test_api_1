# Generated by Django 2.1.7 on 2019-02-26 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0004_auto_20190226_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.CharField(default='YzIqOxNnJP2hk3W-I_IxJ', editable=False, max_length=21, primary_key=True, serialize=False),
        ),
    ]
