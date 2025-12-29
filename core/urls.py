from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index ,  name="index"),
    path("newyear/", views.index ,  name="newyear"),
    path("", views.hello,  name="hello"),
    
]
