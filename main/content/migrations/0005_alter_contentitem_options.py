# Generated by Django 5.0.6 on 2024-07-31 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_filecontent_options_alter_imagecontent_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contentitem',
            options={'ordering': ('order',), 'verbose_name': 'Content item', 'verbose_name_plural': 'Content items'},
        ),
    ]
