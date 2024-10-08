from django.contrib.auth.models import User
from rest_framework import serializers

from main.public.models import News, Event
from main.university.models import Faculty, Department, Project, Personal, FacultySpecialty, FacultyProgram, Success


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        exclude = ('name', 'about', )


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        exclude = ('name', 'about', 'faculty', )


# Programs
class FacultySpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultySpecialty
        exclude = ('name', )


class FacultyProgramSerializer(serializers.ModelSerializer):
    program_items = FacultySpecialtySerializer(many=True)

    class Meta:
        model = FacultyProgram
        exclude = ('name', 'department', )


# Projects
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('name', 'author', 'faculty', 'department', )


class SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Success
        exclude = ('title', 'description', 'faculty', 'department', )


# Personal
class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        exclude = ('full_name', 'department', 'profession', 'about', )


# News
class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        exclude = ('title', 'description', 'department', 'user', )


# Events
class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        exclude = ('title', 'description', 'department', 'user', )


# About faculty
class AboutFacultySerializer(serializers.ModelSerializer):
    about_en = serializers.SerializerMethodField()
    about_ru = serializers.SerializerMethodField()
    about_kk = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = ('id', 'about_ru', 'about_en', 'about_kk', )

    def get_about_en(self, obj):
        request = self.context.get('request')
        about = obj.about_en
        if request and about:
            about = about.replace('/media/', request.build_absolute_uri('/media/'))
        return about

    def get_about_ru(self, obj):
        request = self.context.get('request')
        about = obj.about_ru
        if request and about:
            about = about.replace('/media/', request.build_absolute_uri('/media/'))
        return about

    def get_about_kk(self, obj):
        request = self.context.get('request')
        about = obj.about_kk
        if request and about:
            about = about.replace('/media/', request.build_absolute_uri('/media/'))
        return about


# About department
class AboutDepartmentSerializer(serializers.ModelSerializer):
    about_en = serializers.SerializerMethodField()
    about_ru = serializers.SerializerMethodField()
    about_kk = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'about_ru', 'about_en', 'about_kk', )

    def get_about_en(self, obj):
        request = self.context.get('request')
        about = obj.about_en
        if request and about:
            about = about.replace('/media/', request.build_absolute_uri('/media/'))
        return about

    def get_about_ru(self, obj):
        request = self.context.get('request')
        about = obj.about_ru
        if request and about:
            about = about.replace('/media/', request.build_absolute_uri('/media/'))
        return about

    def get_about_kk(self, obj):
        request = self.context.get('request')
        about = obj.about_kk
        if request and about:
            about = about.replace('/media/', request.build_absolute_uri('/media/'))
        return about
