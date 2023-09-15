from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('rooms', views.rooms, name="rooms"),
    path('room/<pk>', views.room, name="room"),
    path('create_room', views.create_room, name="create_room"),
]