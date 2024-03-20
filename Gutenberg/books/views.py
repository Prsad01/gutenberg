from django.shortcuts import render , HttpResponse
from itertools import chain

from rest_framework import viewsets
from .models import Author, Book, BookAuthors, BookBookshelves, BookLanguages, BookSubjects, Bookshelf, Format, Language, Subject
from .serializers import AuthorSerializer,Customeserializer,BookSerializer, BookAuthorsSerializer, BookBookshelvesSerializer, BookLanguagesSerializer, BookSubjectsSerializer, BookshelfSerializer, FormatSerializer, LanguageSerializer, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination


def return_data(books,request):
    paginator = PageNumberPagination()
    paginated_books = paginator.paginate_queryset(books, request)
    books_data = []

    for book in paginated_books:
        book_serializer = BookSerializer(book)


        authors = book.bookauthors_set.filter(author__name='Carroll, Lewis')
        authors = book.bookauthors_set.all()

        author_serializer = BookAuthorsSerializer(authors, many=True)

    
        languages = book.booklanguages_set.all()
        language_serializer = BookLanguagesSerializer(languages, many=True)

        subjects = book.booksubjects_set.all()
        subject_serializer = BookSubjectsSerializer(subjects, many=True)


        bookshelves = book.bookbookshelves_set.all()
        bookshelf_serializer = BookBookshelvesSerializer(bookshelves, many=True)

        book_data = {
            "title": book_serializer.data.get("title"),
            "author": [author.get("author").get("name") for author in author_serializer.data],
            "language": [lang.get('language').get('code') for lang in language_serializer.data],
            "subjects": [subject.get('subject').get('name') for subject in subject_serializer.data],
            # "bookshelves": [shelf.get('bookshelf').get('name') for shelf in bookshelf_serializer.data],
            "bookshelves": bookshelf_serializer.data
        }
        books_data.append(book_data)
    return paginator.get_paginated_response(books_data)
    return books_data


def filter_by_author(author_q,request):
    authors = BookAuthors.objects.filter(author__name__icontains__in = author_q.split(','))
    all_books = []
    for author in authors:
        book = author.book
        all_books.append(book)
    return return_data(all_books,request)
    
def filter_by_language(lang_q,request):
    print(lang_q.split(','))
    langues = BookLanguages.objects.filter(language__code__in = lang_q.split(','))[:50]
    all_books = []
    for lan in langues:
        book = lan.book
        all_books.append(book)
    return return_data(all_books,request)

def filter_by_title(title_q,request):
    all_books = Book.objects.filter(title__icontains__in = title_q.split(','))
    return return_data(all_books,request)

def filter_by_mime_type(mime_type_q,request):
    formates = Format.objects.filter(mime_type__icontains__in = mime_type_q.split(','))
    all_books = []
    for format in formates:
        book = format.book
        all_books.append(book)
    return return_data(all_books,request)

class CustomeBookGetViewset(APIView):
  
   def get(self, request,pk=None):
       
        languages_q = request.query_params.get('language')
        author_q = request.query_params.get('author')
        title_q = request.query_params.get('title')
        mime_type_q = request.query_params.get('mime_type')

        if mime_type_q is not None:
            return (filter_by_mime_type(mime_type_q,request))
        if author_q is not None:
            return (filter_by_author(author_q,request))
        if languages_q is not None:
            return (filter_by_language(languages_q,request))
        if title_q is not None:
            return (filter_by_title(title_q,request))
        

        if pk is not None:
            try:
                book = Book.objects.get(pk=pk)
            except Book.DoesNotExist:
                return Response({"message": "Book not found"}, status=404)
            book_serializer = BookSerializer(book)

            authors = book.bookauthors_set.all()
            author_serializer = BookAuthorsSerializer(authors, many=True)

            languages = book.booklanguages_set.all()
            language_serializer = BookLanguagesSerializer(languages, many=True)

            subjects = book.booksubjects_set.all()
            subject_serializer = BookSubjectsSerializer(subjects, many=True)

            bookshelves = book.bookbookshelves_set.all()
            bookshelf_serializer = BookBookshelvesSerializer(bookshelves, many=True)

            response_data = {
                "title": book_serializer.data.get("title"),
                "author": [author.get("author").get("name") for author in author_serializer.data],
                "language": [lang.get('language').get('code') for lang in language_serializer.data],
                "subjects": [subject.get('subject').get('name') for subject in subject_serializer.data],
                "bookshelves": bookshelf_serializer.data
            }
            
            return Response(response_data)

        else:
            books = Book.objects.all()[:2994]
            return (return_data(books,request))

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()[:10]
    serializer_class = BookSerializer

class BookAuthorsViewSet(viewsets.ModelViewSet):
    queryset = BookAuthors.objects.all()[:10]
    serializer_class = BookAuthorsSerializer

class BookBookshelvesViewSet(viewsets.ModelViewSet):
    queryset = BookBookshelves.objects.all()
    serializer_class = BookBookshelvesSerializer

class BookLanguagesViewSet(viewsets.ModelViewSet):
    queryset = BookLanguages.objects.all()
    serializer_class = BookLanguagesSerializer

class BookSubjectsViewSet(viewsets.ModelViewSet):
    queryset = BookSubjects.objects.all()
    serializer_class = BookSubjectsSerializer

class BookshelfViewSet(viewsets.ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer

class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



