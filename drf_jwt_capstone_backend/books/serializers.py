from rest_framework import serializers
from .models import Book
from .models import Chapter
from .models import Paragraph

from django.contrib.auth import get_user_model

User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['user', 'title', 'description', 'genre', 'daily_paragraphs', 'daily_txt_reminder',
                  'weekly_txt_summary']


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['book', 'title', 'description', 'chapter_number', 'updated']


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['chapter', 'description', 'paragraph_number', 'updated', 'sentence_1', 'sentence_2', 'sentence_3',
                  'sentence_4', 'sentence_5', 'sentence_6', 'sentence_7', 'sentence_8', 'sentence_9', 'sentence_10',
                  'sentence_11', 'sentence_12']
