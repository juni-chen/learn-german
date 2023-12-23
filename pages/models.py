from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=31, verbose_name="カテゴリ名")

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = "カテゴリ"


class Article(models.Model):

    title = models.CharField(max_length=62, verbose_name="タイトル")
    slug = models.SlugField(verbose_name="URLスラッグ（英語）")
    image = models.ImageField(upload_to="article_image", blank=True, verbose_name="記事のイメージ写真", help_text="登録しない場合は、デフォルトのイメージ写真を使用する")
    categories = models.ManyToManyField(Category, verbose_name="カテゴリ")
    body = models.TextField(verbose_name="本文")
    status = models.PositiveSmallIntegerField(default=1, verbose_name="公開ステータス", help_text="1:下書き, 2:公開")
    liked = models.IntegerField(default=0, verbose_name="いいね数")
    is_deleted = models.BooleanField(default=False, verbose_name="削除フラグ")
    creator = models.CharField(max_length=31, verbose_name="投稿者")
    created = models.DateTimeField(auto_now_add=True, verbose_name="投稿日時")
    modified = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self):
        return self.title

    class Meta:

        verbose_name_plural = "記事"

class Page(models.Model):

    title = models.CharField(max_length=62, verbose_name="タイトル")
    slug = models.SlugField(verbose_name="URLスラッグ（英語）")
    image = models.ImageField(upload_to="article_image", blank=True, verbose_name="記事のイメージ写真", help_text="登録しない場合は、デフォルトのイメージ写真を使用する")
    body = models.TextField(verbose_name="本文")
    status = models.PositiveSmallIntegerField(default=1, verbose_name="公開ステータス", help_text="1:下書き, 2:公開")
    is_deleted = models.BooleanField(default=False, verbose_name="削除フラグ")
    created = models.DateTimeField(auto_now_add=True, verbose_name="投稿日時")
    modified = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self):
        return self.title

    class Meta:

        verbose_name_plural = "ページ"



class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="記事", related_name="comments")
    commenter = models.CharField(max_length=31, verbose_name="コメント者名")
    body = models.TextField(verbose_name="コメント文")
    created = models.DateTimeField(auto_now_add=True, verbose_name="コメント投稿日時")

    def __str__(self):
        return self.article.title + ":{}のコメント".format(self.commenter)

    class Meta:

        verbose_name_plural = "コメント"