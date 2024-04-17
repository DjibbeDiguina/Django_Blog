from django.contrib import admin
from .models import Blog, Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)