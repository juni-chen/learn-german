from django.contrib import admin
from .models import Page
from .models import Article
from .models import Category
from .models import Comment

# Register your models here.
admin.site.register(Page)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)