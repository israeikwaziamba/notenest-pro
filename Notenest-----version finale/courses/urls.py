from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('ajouter/', views.course_add, name='course_add'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
]