from django.urls import path
from .views import blog_title, blog_article

app_name = "blog"

urlpatterns = [
    path('', blog_title, name="blog_title"),
    path('article/<int:article_id>', blog_article, name="blog_article"),
    
]