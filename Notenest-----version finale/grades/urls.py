from django.urls import path
from . import views

urlpatterns = [
    path('', views.grade_list, name='grade_list'),
    path('add/', views.grade_add, name='grade_add'),
    path('stats/', views.grade_stats, name='grade_stats'),
]