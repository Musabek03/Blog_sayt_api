from django.contrib import admin
from .models import Post,Category,Tag



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass