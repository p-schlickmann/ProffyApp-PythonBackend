from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('study/', views.study, name='study'),
    path('teach/', views.teach, name='teach'),
    path('search/', views.search, name='search')
    
]