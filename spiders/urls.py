from django.urls import path
from . import views

app_name = 'species'
urlpatterns = [
    path('', views.home, name='spiders-home'),
    path('spider/<int:spider_id>/', views.specie, name='detail')
]