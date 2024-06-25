from django.urls import path
from .views import guestbook, guestbookpost, guestbookdelete

urlpatterns = [
    path('', guestbook, name='guestbook'),
    path('post/', guestbookpost, name='guestbookpost'),
    path('delete/<int:pk>/', guestbookdelete, name='guestbookdelete'),
]