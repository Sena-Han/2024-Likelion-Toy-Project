from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, Category

def post(request):
    categories = Category.objects.all()
    category_filter = request.GET.get('category')
    posts = Post.objects.filter(author=request.user)
    
    if category_filter:
        posts = posts.filter(category__name=category_filter)
    return render(request, 'post.html', {'posts': posts, 'categories': categories, 'selected_category': category_filter})

def postwrite(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post')
    else:
        form = PostForm()
    return render(request, 'postwrite.html', {'form': form})

def postdelete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    post.delete()
    return redirect('post')