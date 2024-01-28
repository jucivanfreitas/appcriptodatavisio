

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.BASE, name='BASE' ),
    path('home/',views.App, name='App' ),



]
