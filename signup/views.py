from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, MyPageForm
from .models import MyPage

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm() 
    return render(request, 'login.html', {'form': form})

def main(request):
    return render(request, 'main.html')

def home(request):
    return render(request, 'home.html')

def mypage(request):
    try:
        mypage = MyPage.objects.get(user=request.user)
        form = None
    except MyPage.DoesNotExist:
        if request.method == 'POST':
            form = MyPageForm(request.POST)

            if form.is_valid():
                mypage = form.save(commit=False)
                mypage.user = request.user
                mypage.save()
                return redirect('mypage')
        else:
            form = MyPageForm()
        mypage = None
    return render(request, 'mypage.html', {'form': form, 'mypage': mypage, 'user': request.user})