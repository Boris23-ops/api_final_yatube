from django.contrib import admin

from posts.models import Post, Group, Comment, Follow


@admin.register(Post, Group, Comment, Follow)
class BlogAdmin(admin.ModelAdmin):
    pass
