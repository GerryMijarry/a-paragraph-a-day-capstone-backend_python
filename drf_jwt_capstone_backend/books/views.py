from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Book
from .models import Chapter
from .models import Paragraph
from .serializers import BookSerializer
from .serializers import ChapterSerializer
from .serializers import ParagraphSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


# Book Views
class BookList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


# Chapter Views
class ChapterList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        chapters = Chapter.objects.all()
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)


# Paragraph Views
class ParagraphList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        paragraphs = Paragraph.objects.all()
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data)
