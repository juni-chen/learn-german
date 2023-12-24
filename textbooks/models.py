from django.db import models

# Create your models here.

class TextbookCategory(models.Model):

    name = models.CharField(max_length=31, verbose_name="カテゴリ名")

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = "カテゴリ"

class Book(models.Model):

    title = models.CharField(max_length=62, verbose_name="タイトル")
    slug = models.SlugField(verbose_name="URLスラッグ（英語）")
    image = models.ImageField(upload_to="article_image", blank=True, verbose_name="記事のイメージ写真", help_text="登録しない場合は、デフォルトのイメージ写真を使用する")
    categories = models.ManyToManyField(TextbookCategory, verbose_name="カテゴリ")
    body = models.TextField(verbose_name="本文")
    status = models.PositiveSmallIntegerField(default=1, verbose_name="公開ステータス", help_text="1:下書き, 2:公開")
    liked = models.IntegerField(default=0, verbose_name="いいね数")

    def __str__(self):
        return self.title

    class Meta:

        verbose_name_plural = "教科書"