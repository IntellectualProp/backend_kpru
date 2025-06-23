from django.contrib import admin
from django import forms
from .models import WebsiteSetting, BulkImageUpload, BulkImage, IpKnowledge
from django.utils.safestring import mark_safe


class WebsiteSettingForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = WebsiteSetting
        fields = ['tag', 'image_file']

    def save(self, commit=True):
        obj = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')

        if image_file:
            obj.image_binary = image_file.read()
            obj.image_file_name = image_file.name

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


class IpKnowledgeForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = IpKnowledge
        fields = ['title', 'description', 'image_file']

    def save(self, commit=True):
        obj = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')

        if image_file:
            obj.image_binary = image_file.read()
            obj.image_file_name = image_file.name  # if image_file_name exists in the model

        if commit:
            obj.save()
        return obj


class IpKnowledgeAdmin(admin.ModelAdmin):
    form = IpKnowledgeForm
    list_display = ('title', 'description', 'image_preview', 'image_file_name')

    def image_preview(self, obj):
        if obj.image_binary:
            image_url = f'http://localhost:8000/django/preview_image/IpKnowledge/{obj.image_file_name}/'
            return mark_safe(f'<a href="{image_url}" target="_blank">View Image</a>')
        return "No image available"

    def image_file_name(self, obj):
        if obj.image_file_name:
            return obj.image_file_name
        return "No image uploaded"

    image_preview.short_description = "Image Preview"
    image_file_name.short_description = "Image File Name"

    readonly_fields = ['image_preview', 'image_file_name']


class BulkImageForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = BulkImageUpload
        fields = ['images']

    def save(self, commit=True):
        # Don't call super().save(commit) directly
        instance = super().save(commit=False)
        instance.save()  # Ensure the instance is saved to DB and has an ID

        # Save uploaded images
        uploaded_files = self.files.getlist('images')
        for uploaded_file in uploaded_files:
            BulkImage.objects.create(
                upload=instance,
                image_binary=uploaded_file.read(),
                image_file_name=uploaded_file.name
            )
        return instance


class BulkImageUploadAdmin(admin.ModelAdmin):
    form = BulkImageForm
    readonly_fields = ('uploaded_at',)


admin.site.register(BulkImageUpload, BulkImageUploadAdmin)
admin.site.register(WebsiteSetting, WebsiteSettingAdmin)
admin.site.register(IpKnowledge, IpKnowledgeAdmin)
