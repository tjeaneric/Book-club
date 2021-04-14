from django.contrib import admin

# Register your models here.

from .models import Book, Discussion
class BookAdmin(admin.ModelAdmin):
    list_display = ('book', 'read_by')
    ordering = ('-read_by',)
    search_fields = ['book']
    fields = (('book', 'read_by'), 'description')

admin.site.register(Book,BookAdmin)
admin.site.register(Discussion)
