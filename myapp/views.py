from django.apps import apps
from django.http import HttpResponse, Http404
from django.shortcuts import render, HttpResponse
from .models import WebsiteSetting
from mimetypes import guess_type
from django.http import Http404

# Create your views here.


def home(request):
    return render(request, 'home.html')


def todos(request):
    return render(request, 'todos.html', {'todos': WebsiteSetting.objects.all()})


def preview_image(request, model_name, filename):
    try:
        # Dynamically get model by app_label and model_name
        ModelClass = apps.get_model('myapp', model_name)

        if not ModelClass:
            raise Http404("Model not found.")

        obj = ModelClass.objects.get(image_file_name=filename)

        if obj.image_binary:
            mime_type, _ = guess_type(filename)
            return HttpResponse(obj.image_binary, content_type=mime_type or 'application/octet-stream')

        raise Http404("Image binary data not found.")
    except LookupError:
        raise Http404("Model lookup failed.")
    except ModelClass.DoesNotExist:
        raise Http404("Object not found.")
