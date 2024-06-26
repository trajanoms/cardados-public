from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('templates/add_template/', views.add_template, name='add_template'),
    path('templates/add_group/', views.add_group, name='add_group'),
    path('add_inspection/', views.add_inspection, name='add_inspection'),
    path('answer_inspection/<uuid:pk>/', views.answer_inspection, name='answer_inspection'),
]