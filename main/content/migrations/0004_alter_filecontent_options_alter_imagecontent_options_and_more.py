# Generated by Django 5.0.6 on 2024-07-31 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_filecontent_caption_en_filecontent_caption_kk_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filecontent',
            options={'verbose_name': 'File content', 'verbose_name_plural': 'File contents'},
        ),
        migrations.AlterModelOptions(
            name='imagecontent',
            options={'verbose_name': 'Image content', 'verbose_name_plural': 'Image contents'},
        ),
        migrations.AlterModelOptions(
            name='textcontent',
            options={'verbose_name': 'Text content', 'verbose_name_plural': 'Text contents'},
        ),
    ]
