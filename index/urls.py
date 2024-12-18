from django.urls import path
from  . import views

urlpatterns = [
    path ('', views.home_page),
    path('', views.news_home, name='news_home')
]
