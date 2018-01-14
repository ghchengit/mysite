from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn


@login_required(login_url='/account/login')
def article_column(request):
    args = {}
    columns = ArticleColumn.objects.filter(user=request.user)
    args['columns'] = columns
    return render(request, "article/column/article_column.html", args)


# Create your views here.


