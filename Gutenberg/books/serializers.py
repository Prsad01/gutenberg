
from rest_framework import serializers
from .models import Author, Book, BookAuthors, BookBookshelves, BookLanguages, BookSubjects, Bookshelf, Format, Language, Subject



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name'] 



class BookSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Book
        fields = '__all__'

class BookAuthorsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = BookAuthors
        fields = ['id','author']


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = '__all__'

class BookBookshelvesSerializer(serializers.ModelSerializer):
    bookshelf = BookshelfSerializer()
    class Meta:
        model = BookBookshelves
        fields = ['id','bookshelf']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class BookLanguagesSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    class Meta:
        model = BookLanguages
        fields = ['id','language']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class BookSubjectsSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    class Meta:
        model = BookSubjects
        fields = ['id','subject']



class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = '__all__'




      
class Customeserializer(serializers.Serializer):
    book_title = serializers.CharField(source = 'book.title')