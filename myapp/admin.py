from django.contrib import admin
from django import forms
from .models import TodoItem


class TodoItemForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)  # Custom image upload field

    class Meta:
        model = TodoItem
        fields = ['title', 'completed', 'image_file']

    def save(self, commit=True):
        obj = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')

        if image_file:
            obj.image_binary = image_file.read()  # Convert image to binary data
            obj.image_file_name = image_file.name  # Store image file name

        if commit:
            obj.save()
        return obj


class TodoItemAdmin(admin.ModelAdmin):
    form = TodoItemForm
    list_display = ('title', 'completed', 'image_file_name', 'image_preview')

    def image_preview(self, obj):
        if obj.image_binary:
            # Display image as Base64 in the admin interface
            import base64
            encoded_image = base64.b64encode(obj.image_binary).decode('utf-8')
            return f'localhost:8000/binary-image/{obj.pk}/'
        return "No image available"

    def image_file_name(self, obj):
        if obj.image_file_name:
            return obj.image_file_name  # Display the image file name
        return "No image uploaded"

    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"
    image_file_name.short_description = "Image File Name"

    readonly_fields = ['image_preview', 'image_file_name']


admin.site.register(TodoItem, TodoItemAdmin)
