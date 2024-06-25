from django.urls import path
from .views import post, postwrite, postdelete

urlpatterns = [
    path('', post, name='post'),
    path('write/', postwrite, name='postwrite'),
    path('delete/<int:pk>/', postdelete, name='postdelete'),
]