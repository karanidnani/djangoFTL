from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from employee import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import APIView

urlpatterns = [
    #path('',""),
    path('admin/', admin.site.urls),
    path('', views.UserList.as_view()),
    path('time',views.TimeList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)