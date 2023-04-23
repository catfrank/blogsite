from datetime import date

from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


# 名词解释
class Words(models.Model):
    word_title = models.CharField(max_length=100)
    word_detail = models.TextField()

    class Meta:
        # 后台管理页面显示
        verbose_name_plural = 'words'

    def __str__(self):
        return self.word_title


# 句子
class Sentences(models.Model):
    sentence = models.TextField()

    class Meta:
        # 后台管理页面显示
        verbose_name_plural = 'sentences'

    def __str__(self):
        return self.sentence


# 标签
class Tags(models.Model):
    tag = models.CharField(max_length=20)

    class Meta:
        # 后台管理页面显示
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.tag
    

# 文章类型
class ArticleType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


# 文章
class Articles(models.Model):
    # 标题
    title = models.CharField(max_length=50,blank=True)
    # 类型
    article_type = models.ForeignKey(ArticleType, blank=True, null=True, on_delete=models.DO_NOTHING)
    # 文章标签
    tags = models.ManyToManyField(Tags)
    # 文章的创建时间
    created = models.DateField(default=date.today)
    # 最终修改时间
    last_updated_time = models.DateTimeField(auto_now=True)
    # 文章正文
    content = RichTextUploadingField()
    # 标记是否删除
    is_deleted = models.BooleanField(default=False)

    class Meta:
        # 后台管理页面显示
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title
