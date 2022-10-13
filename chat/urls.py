from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/<str:room>/', views.room, name='room'),
    path('create', views.create_room, name='create'),
    path('send/', views.send_message),
    path('getMessages/<str:room>/', views.getMessages)
]
