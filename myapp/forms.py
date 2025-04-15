from django import forms
from .models import WebsiteSetting

class WebsiteSettingForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)  # Temporary field for image upload

    class Meta:
        model = WebsiteSetting
        fields = ['tag', 'image_file']
