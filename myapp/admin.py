from django.contrib import admin
from django import forms
from .models import WebsiteSetting
from django.utils.safestring import mark_safe


class WebsiteSettingForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)  # Custom image upload field

    class Meta:
        model = WebsiteSetting
        fields = ['tag', 'image_file']

    def save(self, commit=True):
        obj = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')

        if image_file:
            obj.image_binary = image_file.read()  # Convert image to binary data
            obj.image_file_name = image_file.name  # Store image file name

        if commit:
            obj.save()
        return obj


class WebsiteSettingAdmin(admin.ModelAdmin):
    form = WebsiteSettingForm
    list_display = ('tag', 'image_preview', 'image_file_name')

    def image_preview(self, obj):
        if obj.image_binary:
            image_url = f'http://localhost:8000/django/preview_image/{obj.image_file_name}/'
            return mark_safe(f'<a href="{image_url}" target="_blank">View Image</a>')
        return "No image available"

    def image_file_name(self, obj):
        if obj.image_file_name:
            return obj.image_file_name  # Display the image file name
        return "No image uploaded"

    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"
    image_file_name.short_description = "Image File Name"

    readonly_fields = ['image_preview', 'image_file_name']


admin.site.register(WebsiteSetting, WebsiteSettingAdmin)
