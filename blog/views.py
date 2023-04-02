from django.shortcuts import render
from django.http import HttpResponse

from .models import Articles, Tags, Words, Sentences

# 主页视图
def index(request):
    articles = Articles.objects.order_by('-created')
    context = {
         'articles_all': articles,
         'tags_all': Tags.objects.all(),
         'words_all': Words.objects.all(),
         'sentences_all': Sentences.objects.all(),
    }
    return render(request, 'index.html', context)

# Programs视图
def programs(request):
    programs = Articles.objects.filter(article_type_id = 1)
    context = {
        'programs': programs,
    }
    return render(request, 'programs.html', context)

# Writings视图
def writings(request):
    writings = Articles.objects.filter(article_type_id = 2)
    context = {
        'writings': writings,
    }
    return render(request, 'writings.html', context)

# Words视图
def words(request):
    words = Words.objects.all()
    context = {
        'words': words,
    }
    return render(request, 'words.html', context)

# Sentences视图
def sentences(request):
    sentences = Sentences.objects.all()
    context = {
        'sentences': sentences,
    }
    return render(request, 'sentences.html', context)