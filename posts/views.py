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
        title = request.POST['title']
        content = request.POST['content']
        new_post = Post(
            title = title,
            content = content
        )
        new_post.save()
        return redirect('post-detail',post_id=new_post.id)
    else:
        post_form = PostForm
    return render(request,'posts/post_form.html',{'form':post_form})