from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('prijsklasse/', views.prijsKlasse_view, name="prijsKlasse"),
    path('tellen/', views.telling_view, name="tellen"),
    path('betaling/', views.betalingView, name='betaling'),
    path('leiders/', views.leider_view, name='leiders'),
    path('leider/<int:leider_id>/', views.leider_detail, name="leiderView"),
    path('leiders/update', views.leider_volgorde, name='leidersUpdate'),
    path('prijsklasse/delete/<int:prijsKlasse_id>/', views.prijsKlasse_delete, name='deletePrijsklasse')
]