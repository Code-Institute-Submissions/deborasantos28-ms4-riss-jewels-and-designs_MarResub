from django.contrib import admin
from .models import BlogEntry, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'title', 'slug')
    search_fields = ['title', 'content']
    inlines = [CommentInline, ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'post', 'body', 'username')
    search_fields = ['username', 'body']


admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(Comment, CommentAdmin)