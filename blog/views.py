from django.shortcuts import render

from .models import Articles, Tags, Words, Sentences

import markdown

def home(request):
    return render(request, 'home.html')

# 主页视图
def index(request):
    articles = Articles.objects.order_by('-created')
    context = {
        'articles_all': articles,
        'tags_all': Tags.objects.all(),
        'words_all': Words.objects.order_by('?')[:3],
        'sentences_all': Sentences.objects.order_by('?')[:7],
    }
    return render(request, 'index.html', context)

# Writings视图
def writings(request):
    writings = Articles.objects.order_by('-created')
    context = {
        'writings': writings,        
    }
    return render(request, 'writings.html', context)

# writing_detail视图
def writing_detail(request, articles_id):
    writing = Articles.objects.get(pk = articles_id)

    # 将md语法渲染成html样式
    writing.content = markdown.markdown(writing.content,
        extensions=[
        # 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    
    context = {
        'writing': writing,
    }
    return render(request, 'writing_detail.html', context)

# Words视图
def words(request):
    words = Words.objects.order_by('-id')
    context = {
        'words': words,
    }
    return render(request, 'words.html', context)

# Sentences视图
def sentences(request):
    sentences = Sentences.objects.order_by('-id')
    context = {
        'sentences': sentences,
    }
    return render(request, 'sentences.html', context)