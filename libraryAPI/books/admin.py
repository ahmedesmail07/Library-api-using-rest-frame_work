from django.contrib import admin

from .models import Book


class BookAdminView(admin.ModelAdmin):
    list_display = ("title", "subtitle")


admin.site.register(Book, BookAdminView)
