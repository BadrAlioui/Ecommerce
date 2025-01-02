
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact_page, name='contact'),
    path('authentication/', include ('authentication.urls')),
    path('', include ('products.urls')),
    path('bag/', include ('bag.urls')),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
