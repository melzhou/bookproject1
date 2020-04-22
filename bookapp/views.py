from django.shortcuts import render
from .models import book
from .models import writing

# Create your views here.

def bookshelf(request):
    book_objects = book.objects.all().order_by('-created')
    return render(request,'bookapp/bookshelf.html',{'book_objects':book_objects})

def detail(request,id):
    book_objects = book.objects.get(id=id)
    return render(request, 'bookapp/detail.html',{'book_objects':book_objects})

def nav(request):
    return render(request, 'bookapp/nav.html')

def about(request):
    return render(request, 'bookapp/about.html')

def article(request):  #model name and view name shouldn't be the same
    writing_objects = writing.objects.all().order_by('-created')
    return render(request, 'bookapp/article.html',{'writing_objects':writing_objects})

def index(request):
    return render(request, 'bookapp/index.html')