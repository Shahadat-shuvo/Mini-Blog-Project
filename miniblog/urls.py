from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'), # miniblog/
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('addpost/', views.addPost, name='addpost'),
    path('updatepost/<int:id>/', views.updatePost, name='updatepost'),
    path('deletepost/<int:id>/', views.deletePost, name='deletepost'),
]