# Generated by Django 2.1.7 on 2019-02-26 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0002_auto_20190226_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.CharField(default='y5Mwl3LPkV0dk9p1PzkyJ', editable=False, max_length=21, primary_key=True, serialize=False),
        ),
    ]
