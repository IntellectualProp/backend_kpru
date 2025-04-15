from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WebsiteSetting
from .serializers import WebsiteSettingSerializer

@api_view(["GET"])
def getSliderImage(request):
    # Filter WebsiteSetting objects where tag equals 'slider_homepage'
    website_setting = WebsiteSetting.objects.filter(tag='slider_homepage')
    
    # Serialize the filtered queryset
    serializer = WebsiteSettingSerializer(website_setting, many=True)
    
    return Response(serializer.data)
