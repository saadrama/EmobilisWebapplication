from django.urls import path
from . import views

urlpatterns = [
 
    path('dish.html', views.dish_html_view, name='dish_html'),
    path('about/all_dishes/', views.about_all_dishes, name='about_all_dishes')

  
]