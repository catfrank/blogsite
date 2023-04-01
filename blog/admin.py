from django.contrib import admin

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
    list_display = ("id", "title", "created", "is_deleted", "article_type")
