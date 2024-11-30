
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('about/',about),
    path('booking/',booking),
    path('menu/',menu),
    path('contact/',contact),
    path('testimonial',testimonial),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
