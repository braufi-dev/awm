from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html',{'posts':posts})

# This is the post detail view and it takes the id argument of a post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
                            status = Post.Status.PUBLISHED,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    '''
    try:
        post = Post.published.get(id = id)
    except Post.DoesNotExist:
        raise Http404("No Posts found!")
    '''
    return render(request, 'blog/post/detail.html', {'post': post})