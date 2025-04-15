from rest_framework import serializers
from myapp.models import WebsiteSetting

class WebsiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteSetting
        fields = '__all__'
        read_only_fields = ['id', 'created_time']  # Make these fields read-only