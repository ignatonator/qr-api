"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from qr_api.models import QrCode
from rest_framework import routers, serializers, viewsets,filters

class QrCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QrCode
        fields = ['link', 'title', 'nickname', 'description']
class QrCodeViewSet(viewsets.ModelViewSet):
    queryset = QrCode.objects.all()
    serializer_class = QrCodeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=title', '=nickname']
router = routers.DefaultRouter()
router.register(r'qrcode', QrCodeViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/',include(router.urls)),
    path('', include('qr_api.urls', namespace='qr_api')),

]
