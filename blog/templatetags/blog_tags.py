from django import template
from blog.models import Post,Category
from django.utils import timezone
register = template.Library()

@register.simple_tag(name = 'totalposts')
def function():
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now)
    return posts

@register.filter
def snippet(value):
    return value[:3]

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts():
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now).order_by('published_date')[:2]
    return {'posts':posts}

@register.inclusion_tag('website/website-latest-posts.html')
def weblatestposts():
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now).order_by('-published_date')[:3]
    return {'posts':posts}


@register.inclusion_tag('blog/blog-next-post.html')
def next_post(p_id):
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now)
    t = 0
    post_id = ''
    p_title = ''
    p_image = ''
    for p in posts:
        if p.id == p_id:
            t = 1
        elif t == 1:
            post_id = p.id
            p_title = p.title
            p_image = p.image.url
            break
    return {'p_id':post_id,'p_title':p_title,'p_image':p_image}
        
@register.inclusion_tag('blog/blog-prev-post.html')
def prev_post(post_id):
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now)
    t = 0
    prev_id = ''
    prev_title = ''
    prev_image = ''
    for p in posts:
        if p.id == post_id:
            t = 1           
            return {'prev_id':prev_id,'prev_title':prev_title,'prev_image':prev_image}
        elif t != 1:
            prev_id = p.id
            prev_title = p.title
            prev_image = p.image.url


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}



    
        


   
