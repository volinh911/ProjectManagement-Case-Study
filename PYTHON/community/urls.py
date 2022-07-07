from django.urls import path

from . import views

urlpatterns = [
    path('', views.questions_list, name="questions_list"),
    path('question/<str:pk>/', views.question_detail, name="question_detail"),
    path('create-question/', views.question_create, name="question_create"),
    path('update-question/<str:pk>/', views.question_update, name="question_update"),
    path('delete-question/<str:pk>/', views.question_delete, name="question_delete"),
]
