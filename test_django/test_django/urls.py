from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
#    path('', views.index),
    path('', views.index),

]

