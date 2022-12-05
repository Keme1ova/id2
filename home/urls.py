from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('home/', views.more, name='more'),
    path('home/<int:id>', views.detail, name='detail'),
]
