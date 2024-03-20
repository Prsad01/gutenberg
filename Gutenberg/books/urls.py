from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AuthorViewSet, BookViewSet, BookAuthorsViewSet, BookBookshelvesViewSet,
    BookLanguagesViewSet, BookSubjectsViewSet, BookshelfViewSet,
    FormatViewSet, LanguageViewSet, SubjectViewSet,CustomeBookGetViewset
)
router = DefaultRouter(trailing_slash=False)



router.register(r'authors', AuthorViewSet, basename='AuthorViewSet')
router.register(r'books', BookViewSet, basename='BookViewSet')
router.register(r'book-authors', BookAuthorsViewSet, basename='BookAuthorsViewSet')
router.register(r'book-bookshelves', BookBookshelvesViewSet, basename='BookBookshelvesViewSet')
router.register(r'book-languages', BookLanguagesViewSet, basename='BookLanguagesViewSet')
router.register(r'book-subjects', BookSubjectsViewSet, basename='BookSubjectsViewSet')
router.register(r'bookshelves', BookshelfViewSet, basename='BookshelfViewSet')
router.register(r'formats', FormatViewSet, basename='FormatViewSet')
router.register(r'languages', LanguageViewSet, basename='LanguageViewSet')
router.register(r'subjects', SubjectViewSet, basename='SubjectViewSet')


urlpatterns = [
    path('custom/', CustomeBookGetViewset.as_view(), name='custom_api1'),
    path('custom/<int:pk>', CustomeBookGetViewset.as_view(), name='custom_api2'),

    # path('custom/', CustomerGetView.as_view(), name='custom_api'),



]
