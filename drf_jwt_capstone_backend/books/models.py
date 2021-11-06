from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    genre = models.CharField(max_length=30)
    daily_paragraphs = models.IntegerField()
    daily_txt_reminders = models.BooleanField(default=False)
    weekly_txt_summary = models.BooleanField(default=False)


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    chapter_number = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)


class Paragraph(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    paragraph_number = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    sentence_1 = models.CharField(max_length=150)
    sentence_2 = models.CharField(max_length=150)
    sentence_3 = models.CharField(max_length=150)
    sentence_4 = models.CharField(max_length=150)
    sentence_5 = models.CharField(max_length=150)
    sentence_6 = models.CharField(max_length=150)
    sentence_7 = models.CharField(max_length=150)
    sentence_8 = models.CharField(max_length=150)
    sentence_9 = models.CharField(max_length=150)
    sentence_10 = models.CharField(max_length=150)
    sentence_11 = models.CharField(max_length=150)
    sentence_12 = models.CharField(max_length=150)
