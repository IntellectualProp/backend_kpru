from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import WebsiteSetting
from .serializers import WebsiteSettingSerializer


@api_view(["GET"])
def getData(request):
    website_setting = WebsiteSetting.objects.all()
    serializer = WebsiteSettingSerializer(website_setting, many=True)
    return Response(serializer.data)
