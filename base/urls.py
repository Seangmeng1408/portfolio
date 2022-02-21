
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.Home,name="home"),
    path('post/', views.Post,name="post"),
    path('update/<slug:slug>/', views.UpdatePost,name="update"),
    path('delete/<slug:slug>/', views.Delete,name="delete"),
    path('views/<slug:slug>/', views.Detail,name="views"),
    path('login/', views.Login,name="login"),
    path('logout/', views.Logout,name="logout"),
    path('contact/', views.Contact,name="contact"),
    path('send/', views.SendEmail,name="sendmail"),
]

