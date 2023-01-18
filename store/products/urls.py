from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
