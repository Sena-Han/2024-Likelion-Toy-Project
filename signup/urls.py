from django.urls import path
from .views import main, signup, login, home, mypage

urlpatterns = [
    path('', main, name='main'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('mypage/', mypage, name='mypage'),
]