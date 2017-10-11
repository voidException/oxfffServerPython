"""dovob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from cmdb import views,rest_views
from django.contrib.auth.models import User
from rest_framework import  routers,serializers,viewsets



# Serializers定义了API的表现.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User  #User还没定义
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets 定义了 视图（view） 的行为.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers 提供了一种简单途径，自动地配置了URL。
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# 使用自动的URL路由，让我们的API跑起来。
# 此外，我们也包括了登入可视化API的URLs。

# router = routers.DefaultRouter()
# router.register(r'idc',rest_views.IDCViewSet)
# router.register(r'host',rest_views.HostViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index),
    url(r'^ajax.do/', views.ajax_get_data),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
