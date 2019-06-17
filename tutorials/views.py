from django.shortcuts import render
from .models import Category, SubCategory, SubSubCategory,Tutorial



def home(request):
    return render(request, 'tutorials/home.html', {'categories':Category.objects.all()})


def sub_cat(request, category):
    sub_cats = SubCategory.objects.filter(sub_cat_parent__cat_slug=category)
    # subsub_cats = SubSubCategory.objects.filter(subsub_cat_parent__sub_cat_parent__cat_slug = category)

    context = {
        'sub_cats': sub_cats,
        # 'subsub_cats': subsub_cats,
    }
    return render(request, 'tutorials/sub_cat.html', context)
    

def tutorials(request, category, sub_category, tutorial):
    sub_cats = SubCategory.objects.filter(sub_cat_parent__cat_slug = category)
    tutorials = Tutorial.objects.filter(tutorial_slug = tutorial)

    context = {
        'sub_cats': sub_cats,
        'tutorials':tutorials,
    }

    return render(request, 'tutorials/tutorials.html', context)

