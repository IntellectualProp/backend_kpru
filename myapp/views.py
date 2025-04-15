from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import WebsiteSetting
from mimetypes import guess_type
from django.http import Http404

# Create your views here.


def home(request):
    return render(request, 'home.html')


def todos(request):
    return render(request, 'todos.html', {'todos': WebsiteSetting.objects.all()})


def preview_image(request, filename):  # ← match URL pattern
    try:
        setting = WebsiteSetting.objects.get(image_file_name=filename)
        if setting.image_binary:
            mime_type, _ = guess_type(filename)
            return HttpResponse(setting.image_binary, content_type=mime_type or 'application/octet-stream')
        raise Http404("Image binary data not found.")
    except WebsiteSetting.DoesNotExist:
        raise Http404("Image not found.")
