from django.shortcuts import redirect, render

from .forms import RoomCreateForm
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

def create_room(request):
    form = RoomCreateForm()
    if request.method == 'POST':
        form = RoomCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('rooms')
    context = {'form': form}
    return render(request, 'playground/room_form.html', context)