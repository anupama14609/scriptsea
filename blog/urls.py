from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('blog/', views.BlogPost, name='blog'),
    path('blog/<str:slug>/', views.BlogPage, name='blog-page'),
    path('search/', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('blog/postComment', views.postComment, name="postComment"),
    
]