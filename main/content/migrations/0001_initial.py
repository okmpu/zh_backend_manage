# Generated by Django 5.0.6 on 2024-07-19 11:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('multiple_content', models.BooleanField(default=False, verbose_name='Multiple content')),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapters',
                'ordering': ('index',),
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('dropdown', models.BooleanField(default=False, verbose_name='Dropdown')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
                'ordering': ('index',),
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.chapter', verbose_name='Chapter')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
                'ordering': ('index',),
            },
        ),
        migrations.CreateModel(
            name='According',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.chapter', verbose_name='Chapter')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'According content',
                'verbose_name_plural': 'According contents',
                'ordering': ('-index',),
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('file', models.FileField(upload_to='category/topic/content/files/', verbose_name='File')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.chapter', verbose_name='Chapter')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'File content',
                'verbose_name_plural': 'File contents',
                'ordering': ('-index',),
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.section', verbose_name='Section'),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='staff/', verbose_name='Image')),
                ('profession', models.CharField(max_length=255, verbose_name='Profession')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.chapter', verbose_name='Chapter')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.content', verbose_name='Content')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Staff content',
                'verbose_name_plural': 'Staff contents',
                'ordering': ('index',),
            },
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.section', verbose_name='Section')),
            ],
            options={
                'verbose_name': 'Subsection',
                'verbose_name_plural': 'Subsections',
                'ordering': ('index',),
            },
        ),
        migrations.AddField(
            model_name='content',
            name='sub_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.subsection', verbose_name='Subsection'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='sub_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.subsection', verbose_name='Subsection'),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.chapter', verbose_name='Chapter')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Text content',
                'verbose_name_plural': 'Text contents',
                'ordering': ('-index',),
            },
        ),
    ]
