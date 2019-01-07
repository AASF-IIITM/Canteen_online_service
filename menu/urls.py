from django.urls import path
from .import views


app_name = 'menu'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # cafeteria/menu/
    path('menu/', views.DetailView.as_view(), name='detail'),

    # cafeteria/menu/sabzi/
    path('menu/Sabzi/', views.SabziView.as_view(), name='Sabzi'),

    path('menu/Breads/', views.BreadsView.as_view(), name='Breads'),

    path('menu/Beverages/', views.BeveragesView.as_view(), name='Beverages'),

    path('menu/Thali/', views.ThaliView.as_view(), name='Thali'),

    path('menu/Snacks/', views.SnacksView.as_view(), name='Snacks'),

    path('menu/Street Food/', views.StreetFoodView.as_view(), name='Street Food'),

    path('menu/Rice/', views.RiceView.as_view(), name='Rice'),

    path('menu/Desserts/', views.DessertsView.as_view(), name='Desserts'),



]
