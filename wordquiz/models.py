from django.db import models

# Create your models here.

#単語のカテゴリ分け（「動物」「乗り物」「移動を表す動詞」などを想定）
class WordCategory(models.Model):

    name = models.CharField(max_length=31, verbose_name="単語カテゴリ")

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = "単語カテゴリ"

#個別の問題の構造。単語カテゴリ、ドイツ語の単語とその和訳、解説で構成される
class Problem(models.Model):

    categories = models.ManyToManyField(WordCategory, verbose_name="単語カテゴリ")
    word = models.CharField(max_length=62, verbose_name="単語")
    answer = models.CharField(max_length=62, verbose_name="答え")
    explanation = models.TextField(verbose_name="解説")

    def __str__(self):
        return self.word
    
    class Meta:
        verbose_name = "問題"
        verbose_name_plural = "問題セット"