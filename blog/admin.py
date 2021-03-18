from django.contrib import admin

from .models import Blogger, Comment, Post

admin.site.register(Blogger)
admin.site.register(Comment)


class CommentsInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]
