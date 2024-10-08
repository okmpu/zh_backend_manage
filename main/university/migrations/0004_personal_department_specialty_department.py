# Generated by Django 5.0.6 on 2024-08-12 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_alter_specialty_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='department_personals', to='university.department', verbose_name='Department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='department_specialities', to='university.department', verbose_name='Department'),
            preserve_default=False,
        ),
    ]
