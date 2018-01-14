from django.urls import path
from .views import article_column

app_name = "article"

urlpatterns = [
    path('article-column/', article_column, name="article_column"),
    
]