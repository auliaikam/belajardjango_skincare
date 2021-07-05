from django.contrib import admin
from django.db import models
from .models import Category, Product

def set_available(modeladmin, request, queryset):
    for category in queryset:
        category.available=True
        category.save()

def not_available(modeladmin, request, queryset):
    for category in queryset:
        category.available=False
        category.save()

# set_available.decription = "Make Available Active"

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'available')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = [set_available, not_available]
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'category','created_on')
    search_fields = ['title', 'content']
  
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)