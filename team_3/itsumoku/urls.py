from django.urls import path
from . import views

app_name = 'itsumoku'
urlpatterns = [
    path('index', views.index, name = 'index'),
    path('result',views.result,name='result')
]