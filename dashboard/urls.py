from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Extract elements of URL and make them available as arguments to views.filtered"
    re_path(r"^filtered/(?P<column>.+)/(?P<filter>.+)$", views.filtered, name="filtered"),
    path('addvariant', views.addvariant, name='addvariant'),
    path('createvariant', views.createvariant, name='createvariant'),
    path('editvariant/<int:pk>', views.editvariant, name='editvariant'),
    path('summary', views.summary, name='summary'),  
]
