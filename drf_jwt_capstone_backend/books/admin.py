from django.contrib import admin
from .models import Book
from .models import Chapter
from .models import Paragraph

# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Paragraph)
