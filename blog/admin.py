from django.contrib import admin
from .models import Post, Category, Profile, Comment

# Register your models here.
class PostInCategory(admin.TabularInline):
    model = Post
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [PostInCategory]

class CommentsForPost(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    inlines = [CommentsForPost]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Comment)
