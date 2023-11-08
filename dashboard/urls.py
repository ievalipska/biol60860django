from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addvariant', views.addvariant, name='addvariant'),
    path('createvariant', views.createvariant, name='createvariant'),
]
