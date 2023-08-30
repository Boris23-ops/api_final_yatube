from django.contrib import admin

from posts.models import Comment, Follow, Group, Post


@admin.register(Post, Group, Comment, Follow)
class PostAdmin(admin.ModelAdmin):
    pass
