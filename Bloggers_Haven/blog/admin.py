from django.contrib import admin
from .models import Post, Category, Comment,Article

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date_posted')
    list_filter = ('date_posted', 'category')
    search_fields = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('content',)

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','author', 'category', 'created_at')
    list_filter=('created_at', 'category')
    search_fields=('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article,ArticleAdmin)