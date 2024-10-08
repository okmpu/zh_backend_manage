# Generated by Django 5.0.6 on 2024-08-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_alter_filecontent_content_alter_imagecontent_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffcontent',
            name='call',
            field=models.CharField(default='', max_length=32, verbose_name='Call'),
        ),
        migrations.AddField(
            model_name='staffcontent',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=64, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='staffcontent',
            name='room',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Room'),
        ),
        migrations.AlterField(
            model_name='staffcontent',
            name='phone',
            field=models.CharField(default='', max_length=32, verbose_name='Phone'),
        ),
    ]
