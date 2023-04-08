from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index),
    path('search',views.search),
    path('aboutme/',views.aboutme,name='aboutme'),
    path('abtp/',views.abtp),
    path('image/',views.img)
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
