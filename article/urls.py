from django.urls import path
from .views import article_column, rename_article_column, del_article_column

app_name = "article"

urlpatterns = [
    path('article-column/', article_column, name="article_column"),
    path('rename-column/', rename_article_column, name="rename_article_column"),
    path('del-column/', del_article_column, name="del_article_column"),
    
]