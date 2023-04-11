import markdown

from django.shortcuts import render

from .models import Articles, Tags, Words, Sentences

def home(request):
    return render(request, 'home.html')

# 主页视图
def index(request):
    articles = Articles.objects.order_by('-created')
    context = {
        'articles_all': articles,
        'tags_all': Tags.objects.all(),
        'words_all': Words.objects.order_by('?')[:2],
        'sentences_all': Sentences.objects.order_by('?')[:15],
    }
    return render(request, 'index.html', context)

# Programs视图
def programs(request):
    programs = Articles.objects.filter(article_type_id = 1)
    context = {
        'programs': programs,
    }
    return render(request, 'programs.html', context)

# program_detail视图
def program_detail(request, articles_id):
    program = Articles.objects.get(pk = articles_id)
    # 后台editor富文本编辑
    context = {
        'program': program,
    }

    # 后台markdown语法编辑
    # 将markdown语法渲染成html样式
    # program.content = markdown.markdown(program.content,
    #     extensions=[
    #     # 包含 缩写、表格等常用扩展
    #     'markdown.extensions.extra',
    #     # 语法高亮扩展
    #     'markdown.extensions.codehilite',
    #     ])
    context = {'program': program}
    return render(request, 'program_detail.html', context)

# Writings视图
def writings(request):
    writings = Articles.objects.filter(article_type_id = 2)
    context = {
        'writings': writings,        
    }
    return render(request, 'writings.html', context)

# writing_detail视图
def writing_detail(request, articles_id):
    writing = Articles.objects.get(pk = articles_id)
    context = {
        'writing': writing,
    }
    return render(request, 'writing_detail.html', context)

# Words视图
def words(request):
    words = Words.objects.all()
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