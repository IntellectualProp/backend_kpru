from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.


def home(request):
    return render(request, 'home.html')


def todos(request):
    return render(request, 'todos.html', {'todos': TodoItem.objects.all()})


def show_binary_image(request, pk):
    item = TodoItem.objects.get(pk=pk)
    if item.image_binary:
        # or 'image/jpeg'
        return HttpResponse(item.image_binary, content_type='image/png')
    return HttpResponse("No binary image found", status=404)
