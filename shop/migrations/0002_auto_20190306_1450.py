# Generated by Django 2.1.7 on 2019-03-06 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='customers',
            field=models.ManyToManyField(through='shop.Membership', to='shop.Customer'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='shop.Customer'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Group'),
        ),
    ]
