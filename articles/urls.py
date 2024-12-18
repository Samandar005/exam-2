from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('create/', views.create_post, name='create'),
    path('category/<str:category>/', views.article_category, name='category'),
    path('detail/<int:pk>/', views.article_detail, name='detail'),
]
