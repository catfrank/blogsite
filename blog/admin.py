from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Words, Sentences, Tags, ArticleType, Articles


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ("id", "word_title")


@admin.register(Sentences)
class SentencesAdmin(admin.ModelAdmin):
    list_display = ("id","sentence")


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("id", "tag")


@admin.register(ArticleType)
class ArticleType(admin.ModelAdmin):
    list_display = ("id", "type_name")


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':150, 'cols':150})},
    }
    list_display = ("id", "title", "created", "is_deleted", "article_type")
