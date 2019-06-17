from django.urls import path
from . import views as tut_views


app_name = 'tutorials'
urlpatterns = [
    path('', tut_views.home, name='home'),
    path('<slug:category>/', tut_views.sub_cat, name='sub_cats'),
    path('<slug:category>/<slug:sub_category>/<slug:tutorial>/', tut_views.tutorials, name='tutorials'),

]

