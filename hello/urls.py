from django.urls import path
from .views import index, megha, hello, greet

urlpatterns = [
    path('', index, name='index'),
    path('hello/', hello, name='hello'),
    path('megha/', megha, name='megha'),
    path('<str:name>/', greet, name='greet'),
    
]
