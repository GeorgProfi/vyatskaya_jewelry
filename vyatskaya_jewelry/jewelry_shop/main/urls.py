from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.catalog,name='Global' ),
    path('about', views.about,name='about' ),
    path('show', views.display_images, ),
    path('<int:product_id>',views.detail, name='detail'),
    path('catalog', views.catalog,name = 'catalog'),

]

if settings.DEBUG:
    urlpatterns+=staticfiles_urlpatterns()+static(
        settings.MEDIA_URL, document_root= settings.MEDIA_ROOT
    )