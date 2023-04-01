from django.shortcuts import render
from django.http import HttpResponse

from .models import Articles, Tags, Words, Sentences


def index(request):
    articles = Articles.objects.order_by('-created')
    context = {
         'articles_all': articles,
         'tags_all': Tags.objects.all(),
         'words_all': Words.objects.all(),
         'sentences_all': Sentences.objects.all(),
    }
    return render(request, 'index.html', context)

    