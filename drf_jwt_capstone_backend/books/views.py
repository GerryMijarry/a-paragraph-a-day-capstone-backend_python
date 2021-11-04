from django.http.response import Http404
from django.shortcuts import render

from .models import Book
from .models import Chapter
from .models import Paragraph

from .serializers import BookSerializer
from .serializers import ChapterSerializer
from .serializers import ParagraphSerializer


from django.contrib.auth import get_user_model

User = get_user_model()



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Book Views
class BookList(APIView):

    def get(self, request, bookid):
        comment = Comment.objects.filter(bookid=bookid)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):

    def get_object(self, id):
        try:
            return Book.objects.filter(id=id)
        except Book.DoesNotExist:
            raise Http404

    #get by book id
    def get(self, request, id):
        book = self.get_object(id)
        serializer = CommentSerializer(book, many=True)
        return Response(serializer.data)

    #update
    def put(self, request, id):
        book = self.get_object(id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, bookid):
        book = self.get_object(bookid)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Chapter Views
