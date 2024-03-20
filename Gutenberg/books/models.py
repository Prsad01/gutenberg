from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    download_count = models.IntegerField(null=True, blank=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'books_book'


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    birth_year = models.SmallIntegerField(null=True, blank=True)
    death_year = models.SmallIntegerField(null=True, blank=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'books_author'


class BookAuthors(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_authors'



class Bookshelf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'books_bookshelf'

class Format(models.Model):
    id = models.AutoField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_format'



class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        db_table = 'books_subject'



class BookBookshelves(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_bookshelves'




class Language(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=4)

    class Meta:
        db_table = 'books_language'

class BookLanguages(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_languages'

class BookSubjects(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_subjects'

