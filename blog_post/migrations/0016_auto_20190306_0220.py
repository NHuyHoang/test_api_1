# Generated by Django 2.1.7 on 2019-03-06 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0015_auto_20190304_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.CharField(default='WCTp3GzuyoqUeIwRG5e81', editable=False, max_length=21, primary_key=True, serialize=False),
        ),
    ]