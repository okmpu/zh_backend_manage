from django.db import models
from django.utils.translation import gettext_lazy as _


# Faculty
class Faculty(models.Model):
    FACULTY_TYPE = (
        ('DEFAULT', _('Default')),
        ('INSTITUTE', _('Institute')),
        ('COLLEGE', _('College')),
    )
    name = models.CharField(_('Name'), max_length=128)
    slug = models.CharField(_('Slug'), max_length=128)
    image = models.ImageField(_('Image'), upload_to='university/faculties/avatars', null=True, blank=True)
    poster = models.ImageField(_('Poster'), upload_to='university/faculties/posters', null=True, blank=True)
    faculty_type = models.CharField(_('Faculty type'), choices=FACULTY_TYPE, default='DEFAULT', max_length=16)
    about = models.TextField(_('About'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')


class Department(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='departments', verbose_name=_('Faculty')
    )
    name = models.CharField(_('Name'), max_length=128)
    slug = models.CharField(_('Slug'), max_length=128)
    about = models.TextField(_('About'), blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.faculty.name, self.name)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')


# Programs
class Program(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    slug = models.SlugField(_('Slug'), max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')


class Specialty(models.Model):
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE,
        related_name='program_items', verbose_name=_('Program')
    )
    code = models.CharField(_('Code'), max_length=128)
    name = models.CharField(_('Name'), max_length=128)

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)
