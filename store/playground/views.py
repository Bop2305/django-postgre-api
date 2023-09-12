from django.shortcuts import render
from .models import Room, Message

# Create your views here.


def home(request):
    return render(request, 'playground/home.html')


def rooms(request):
    rooms = Room.objects.all()
    messages = Message.objects.all()
    context = {'rooms': rooms, 'messages': messages}
    for message in messages:
        print(message.room)
    return render(request, 'playground/room.html', context)


def room(request, pk):
    if (type(pk) == str):
        print(pk)
    context = {'pk': pk}
    return render(request, 'playground/room.html', context)
