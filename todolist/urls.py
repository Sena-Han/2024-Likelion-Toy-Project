from django.urls import path
from .views import todolist, tododetail, todopost, todoedit, tododone, tododonelist

urlpatterns = [
    path('', todolist, name='todolist'),
    path('detail/<int:pk>/', tododetail, name='tododetail'),
    path('post/', todopost, name='todopost'),
    path('<int:pk>/edit/', todoedit, name='todoedit'),
    path('done/<int:pk>/', tododone, name='tododone'),
    path('done/', tododonelist, name='tododonelist'),
]