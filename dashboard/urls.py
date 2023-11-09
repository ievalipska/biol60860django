from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Extract elements of URL and make them available as arguments to views.filtered"
    

    path('addvariant', views.addvariant, name='addvariant'),
    path('createvariant', views.createvariant, name='createvariant'),
]
