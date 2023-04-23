from django.urls import path

from . import views

urlpatterns = [
    # 主页（欢迎页）
    path('', views.home, name='home'),
    # 索引页
    path('index/', views.index, name='index'),
    # writings文章列表页
    path('writings/', views.writings, name='writings'),
    # words内容页
    path('words/', views.words, name='words'),
    # sentences内容页
    path('sentences/', views.sentences, name='sentences'),
    # writings类型下具体某篇文章
    path('writingss/<int:articles_id>', views.writing_detail, name='writing_detail'),
]