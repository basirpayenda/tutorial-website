from django.contrib import admin

from .models import Category, SubCategory, SubSubCategory, Tutorial

class CategoryAdmin(admin.ModelAdmin):
    fields = [
        'cat_title',
        'cat_overview',
        'cat_image',
    ]

class SubCategoryAdmin(admin.ModelAdmin):
    fields = [
        'sub_cat_title',
        'sub_cat_overview',
        'sub_cat_parent',
        'sub_cat_image',
    ]


class TutorialAdmin(admin.ModelAdmin):
    fields = [
        'tutorial_title',
        'tutorial_parent',
        'tutorial_author',
        'tutorial_views',
        'tutorial_content',
        'tutorial_thumbnail',
    ]

class SubSubCategoryAdmin(admin.ModelAdmin):
    fields = [
        'subsub_cat_title',
        'subsub_cat_parent'
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(SubSubCategory, SubSubCategoryAdmin)


