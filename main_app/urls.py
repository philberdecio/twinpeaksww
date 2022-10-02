from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('about/', views.About.as_view(), name = "about"),
    path('characters/', views.CharacterList.as_view(), name="character_list")
]