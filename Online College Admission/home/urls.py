from django.contrib import admin
from django.urls import path,include
from home import views
#dummy
#from .views import HomePageView, CreatePostView
#dummy

urlpatterns = [
    path('',views.index, name="home"),
    #dummy1
    path("contact",views.contact, name='contact'),
    path('register', views.registerPage, name='register'),
    path('blog', views.blog, name='blog'),
    #dummy1

    #dummy
    #path('', HomePageView.as_view(), name='home'),
    #path('post/', CreatePostView.as_view(), name='add_post'),
    #dummy
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
]





