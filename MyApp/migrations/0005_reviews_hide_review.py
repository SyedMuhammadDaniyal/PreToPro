# Generated by Django 3.0.6 on 2020-07-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='hide_review',
            field=models.CharField(default='', max_length=10),
        ),
    ]
