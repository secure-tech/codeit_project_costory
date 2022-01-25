from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    cont = {"posts":posts}
    return render(request,'posts/post_list.html',cont)

def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)
    cont = {'post':post}
    return render(request,'posts/post_detail.html',cont)

def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect('post-detail',post_id=new_post.id)
    else:
        post_form = PostForm
    return render(request,'posts/post_form.html',{'form':post_form})

def post_update(request,post_id):
    post = Post.objects.get(id=post_id)
    if (request.method == 'POST'):
        post_form = PostForm(request.POST,instance=post)
        if (post_form.is_valid()):
            post_form.save()
            return redirect('post-detail',post_id=post.id)
    else:
        post_form = PostForm(instance=post)
    return render(request,'posts/post_form.html',{'form':post_form})

def post_delete(request,post_id):
    post = Post.objects.get(id=post_id)
    if (request.method == 'POST'):
        post.delete()
        return redirect('post-list')
    else:
        return render(request,'posts/post_confirm_delete.html',{'post':post})