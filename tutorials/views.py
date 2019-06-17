from django.shortcuts import render
from .models import Category, SubCategory, Tutorial



def home(request):
    return render(request, 'tutorials/home.html', {'categories':Category.objects.all()})


def sub_cat(request, category):
    categories = Category.objects.all()
    sub_cats = SubCategory.objects.filter(sub_cat_parent__cat_slug=category)

    context = {
        'sub_cats': sub_cats, 
        'categories': categories
    }
    return render(request, 'tutorials/sub_cat.html', context )

def tutorials(request, category ,sub_cat):
    categories = Category.objects.all()
    sub_cats = SubCategory.objects.filter(sub_cat_parent__cat_slug=category)
    tutorials = Tutorial.objects.filter(tutorial_parent__sub_cat_slug = sub_cat)
    
    context = {
        'tutorials': tutorials,
        'sub_cats': sub_cats, 
        'categories': categories
    }
    return render(request, 'tutorials/tutorials.html', context)

