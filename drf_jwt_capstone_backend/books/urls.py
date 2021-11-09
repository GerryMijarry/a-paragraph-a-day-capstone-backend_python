from django.urls import path
from books import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('books/', views.BookList.as_view()),
    path('chapters/', views.ChapterList.as_view()),
    path('paragraphs/', views.ParagraphList.as_view()),
]
