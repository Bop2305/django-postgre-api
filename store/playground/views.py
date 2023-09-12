from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'playground/home.html')

def room(request, pk):
    if(type(pk) == str):
        print(pk)
    context = {'pk': pk}
    return render(request, 'playground/room.html', context)