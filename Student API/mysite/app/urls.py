
from django.contrib import admin
from django.urls import path,include
from .views import Studentviewset

from .views import Studentviewset
from  rest_framework import  routers

routers=routers.DefaultRouter()
routers.register(r'students',Studentviewset)

urlpatterns = [
    path("",include(routers.urls)),
    path('admin/', admin.site.urls),
]
