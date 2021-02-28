from django.shortcuts import render,HttpResponse
from .models import SignsList,Blogmodel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BlogForm
from django.shortcuts import  get_object_or_404
from taggit.models import Tag
from django.db.models import Q


def Home(request):
    SignsLists = SignsList.objects.all()
    arti = Blogmodel.objects.all().order_by('-id')[:6]
    args = {'SignsLists':SignsLists,'arti':arti}
    return render(request,'index.html',args)

def read_file(request):
    return HttpResponse('google.com, pub-8283141263662455, DIRECT, f08c47fec0942fa0')

def read_google(request):
    return HttpResponse('google-site-verification: google2fa4526cbb5e6784.html')

def singCategory(request,slug,cat):
    sign = SignsList.objects.get(Title=slug)
    articled = Blogmodel.objects.all()
    args = {'sign':sign, 'cat':cat, 'slug':slug,'articled':articled}
    return render(request,'base3.html',args)



def blog_list(request):
    articles = Blogmodel.objects.all().order_by('-id')

    paginator = Paginator(articles, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    articles = paginator.get_page(page)


    args = {'articles':articles,'posts': posts }
    return render(request,'blog.html',args)

def tagged(request, slug):

    query = Q(body__icontains=slug ) | Q(Title__icontains=slug )
    articles = Blogmodel.objects.filter(query).order_by('-id')

    paginator = Paginator(articles, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    articles = paginator.get_page(page)


    args = {'articles':articles,'posts': posts }
    return render(request,'blog.html',args)

def flower(request):
    yvavili = Blogmodel.objects.all().order_by('-id')[:6]
    args = {'yvavili':yvavili }
    return render(request,"gvirila.html",args)

def blogDetail(request, slug):
    article = Blogmodel.objects.get(slug=slug)
    articlee = Blogmodel.objects.all().order_by('-id')[:10]
    

    if article.tags:
        common_tags = article.tags.split(',')
    else:
        common_tags = []

    args = {'article':article,"articlee":articlee,'common_tags':common_tags}
    return render(request,'blogdetail.html',args)

def error_404_view(request, exception):
    return render(request,'html2/404.html')

