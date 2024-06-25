from django.shortcuts import render, redirect, get_object_or_404
from .forms import GuestBookForm
from .models import GuestBook

def guestbook(request):
    guestBooks = GuestBook.objects.filter(author=request.user).order_by('-write_time')
    return render(request, 'guestbook.html', {'guestBooks': guestBooks})

def guestbookpost(request):
    if request.method == 'POST':
        form = GuestBookForm(request.POST)

        if form.is_valid():
            guestbook = form.save(commit=False)
            guestbook.author = request.user
            guestbook.save()
            return redirect('guestbook')
    else:
        form = GuestBookForm()
    return render(request, 'guestbookpost.html', {'form': form})

def guestbookdelete(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk, author=request.user)
    guestbook.delete()
    return redirect('guestbook')