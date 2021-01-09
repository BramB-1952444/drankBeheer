from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('prijsklasse/', views.prijsKlasse_view, name="prijsKlasse"),
    path('tellen/', views.telling_view, name="tellen"),
    path('betaling/', views.prijsKlasse_view, name='betaling'),
    path('leiders/', views.prijsKlasse_view, name='leiders'),
    path('prijsklasse/delete/<int:prijsKlasse_id>/', views.prijsKlasse_delete, name='deletePrijsklasse')
]