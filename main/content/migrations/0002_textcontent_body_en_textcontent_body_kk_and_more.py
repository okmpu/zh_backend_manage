# Generated by Django 5.0.6 on 2024-07-31 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textcontent',
            name='body_en',
            field=models.TextField(blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='textcontent',
            name='body_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='textcontent',
            name='body_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Body'),
        ),
    ]
