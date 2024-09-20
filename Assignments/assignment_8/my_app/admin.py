from importlib import resources
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from my_app.models import Author, Book


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    list_filter = ('author', )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', )
    search_fields = ('name', )


