from django.urls import path
from  . import views

urlpatterns = [
    path ('', views.home_page),
    path('', views.news_home, name='news_home'),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
    path('news/<int:news_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_news, name='favorite_news')
]
