from django.contrib import admin
from django.urls import path
from .views import first_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_page),
]
