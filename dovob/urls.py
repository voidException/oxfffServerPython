

from django.conf.urls import url, include
from django.contrib import admin
from cmdb import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index),
    url(r'^loginaction/',views.loginaction),
    url(r'^ajax.pp/', views.ajax_get_data),
    url(r'^help/newslist.pp',views.newslist),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
