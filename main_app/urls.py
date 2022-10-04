from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('about/', views.About.as_view(), name = "about"),
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/new/', views.CharacterCreate.as_view(), name="character_create"),
    path('artists/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/update',views.CharacterUpdate.as_view(), name="character_update")
]