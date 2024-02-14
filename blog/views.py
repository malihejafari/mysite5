from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def blog_view(request,**kwargs):
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)



def blog_single(request,pid):
    now = timezone.now()
    post = get_object_or_404(Post,pk=pid,status=1,published_date__lte=now)
    post.counted_views += 1 
    post.save()
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

def blog_category(request,cat_name):
    now = timezone.now()
    #posts = get_object_or_404(Post,status=1,published_date__lte=now)
    posts = Post.objects.filter(status=1,published_date__lte=now)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    now = timezone.now()
    #posts = get_object_or_404(Post,status=1,published_date__lte=now)
    posts = Post.objects.filter(status=1,published_date__lte=now)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)



