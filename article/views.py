from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import ArticleColumn
from .forms import ArticleColumnForm


@login_required(login_url='/account/login')
@csrf_exempt
def article_column(request):
    args = {}
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        args.update({'columns':columns, 'column_form':column_form})
        return render(request, "article/column/article_column.html", args)
    if request.method == "POST":
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)
        if columns:
            return HttpResponse("2")
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse("1")
            
            
@login_required(login_url='/account/login')
#@require_POST
@csrf_exempt
def rename_article_column(request):
    if request.method == "GET":
        return HttpResponse("1111111111")
    column_name = request.POST["column_name"]
    column_id = request.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)   
        line.column = column_name   
        line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("0")
        
        
@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete() 
        return HttpResponse("1")
    except:
        return HttpResponse("2")

# Create your views here.


