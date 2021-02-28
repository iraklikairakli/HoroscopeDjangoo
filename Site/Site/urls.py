
from django.contrib import admin
from django.urls import path,include
from django.views.static import serve 

from django.contrib.sitemaps.views import sitemap
from my_site.sitemaps import BlogSitemap,SingSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {'blog':BlogSitemap,'sign':SingSitemap}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('', include('my_site.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},name = "jango.contrib.sitemaps.views.sitemap"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = 'my_site.views.error_404_view'
