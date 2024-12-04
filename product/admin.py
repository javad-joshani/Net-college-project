from django.contrib import admin
from .models import (Product,
                     Category,
                     Gallery,
                     ProductSpecification,
                     ProductSpecificationValue,
                     Color,
                    )



admin.site.register(Color)

class ProductSpecificationAdmin(admin.TabularInline):
    model = ProductSpecification
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title","parent","humanuze_date"]
    prepopulated_fields = {"slug": ["title"]}
    inlines = [ProductSpecificationAdmin]


class GalleryAdmin(admin.TabularInline):
    model = Gallery
    extra = 1


class ProductSpecificationValueAdmin(admin.TabularInline):
    model = ProductSpecificationValue
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","number","price","thumbnail"]
    inlines = [GalleryAdmin,ProductSpecificationValueAdmin]
    
    
