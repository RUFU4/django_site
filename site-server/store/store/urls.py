"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import index
from products.views import aboutus
from products.views import catalog
from products.views import contact
from products.views import faq
from products.views import basket
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', aboutus, name='aboutus'),
    path('catalog/', catalog, name='catalog'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('add/', include('products.urls', namespace='products')),
    path('basket/', basket, name='basket'),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
