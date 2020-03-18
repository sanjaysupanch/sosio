from django.contrib import admin
from django.urls import path, include
from tutorial import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorial/', include('tutorial.urls')),
]
