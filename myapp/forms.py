from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)  # Temporary field for image upload

    class Meta:
        model = TodoItem
        fields = ['title', 'completed', 'image_file']
