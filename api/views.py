from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import WebsiteSetting, IpKnowledge
from .serializers import WebsiteSettingSerializer, IpKnowledgeSerializer


@api_view(["GET"])
def getSliderImage(request):
    website_setting = WebsiteSetting.objects.filter(tag='slider_homepage')
    serializer = WebsiteSettingSerializer(website_setting, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getIpKnowledge(request):
    ip_knowledge = IpKnowledge.objects.all()
    serializer = IpKnowledgeSerializer(ip_knowledge, many=True)
    return Response(serializer.data)
