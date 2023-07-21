from django.contrib import admin
from app1.models import Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'subject']

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'release_date', 'rating']
admin.site.register(Book, BookAdmin)