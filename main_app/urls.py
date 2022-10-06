from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('about/', views.About.as_view(), name = "about"),
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/new/', views.CharacterCreate.as_view(), name="character_create"),
    path('artists/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/update',views.CharacterUpdate.as_view(), name="character_update"),
    path('characters/<int:pk>/delete', views.CharacterDelete.as_view(), name="character_delete"),
    path('characters/<int:pk>/quotes/new', views.QuoteCreate.as_view(), name="quote_create"),
    path('quote-lists/', views.QuoteLists.as_view(), name="quote_lists"),
    path('quotelists/<int:pk>/quotes/<int:quote_pk>/', views.QuotelistQuoteAssoc.as_view(), name="quotelist_quote_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]
