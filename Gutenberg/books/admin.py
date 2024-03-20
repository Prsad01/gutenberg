from django.contrib import admin
from .models import Author, Book, BookAuthors, BookBookshelves, BookLanguages, BookSubjects, Bookshelf, Format, Language, Subject

# List of all models
models_list = [Author, Book, BookAuthors, BookBookshelves, BookLanguages, BookSubjects, Bookshelf, Format, Language, Subject]

# Register all models
for model in models_list:
    admin.site.register(model)
