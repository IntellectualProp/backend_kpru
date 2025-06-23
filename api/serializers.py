from rest_framework import serializers
from myapp.models import WebsiteSetting, IpKnowledge


class WebsiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteSetting
        fields = '__all__'
        read_only_fields = ['id', 'created_time']


class IpKnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpKnowledge
        fields = '__all__'
        read_only_fields = ['id', 'created_time']
