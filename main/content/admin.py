from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationTabularInline
from django_summernote.admin import SummernoteModelAdminMixin
from .models import Category, Content, TextContent, FileContent, ImageContent, StaffContent


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'app_name', 'parent', 'multiple', 'order', )
    list_filter = ('parent', 'app_name', 'multiple',)
    search_fields = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name_en', )}


class TextContentTabular(SummernoteModelAdminMixin, TranslationTabularInline):
    model = TextContent
    extra = 0


class FileContentTabular(TranslationTabularInline):
    model = FileContent
    extra = 0


class ImageContentTabular(admin.TabularInline):
    model = ImageContent
    extra = 0


class StaffContentTabular(TranslationTabularInline):
    model = StaffContent
    extra = 0


class ContentAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'category', 'order', )
    list_filter = ('category',)
    search_fields = ('title', 'slug', )
    prepopulated_fields = {'slug': ('title_en', )}
    inlines = [TextContentTabular, ImageContentTabular, FileContentTabular, StaffContentTabular, ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)
