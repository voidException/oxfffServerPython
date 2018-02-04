

from django.conf.urls import url, include
from django.contrib import admin
from cmdb import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)




urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/',views.index),
    url(r'^loginaction/',views.loginaction),
    url(r'^ajax.pp/', views.ajax_get_data),
    url(r'^help/newslist.pp',views.newslist),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-auth/', include('rest_framework.urls'))
]
