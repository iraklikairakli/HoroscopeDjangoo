from django.urls import path
from .views import singCategory,Home,blog_list,blogDetail,read_file,tagged,read_google,flower
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.views.generic import TemplateView

urlpatterns = [
    path('',Home,name= "Home"),
    path('horoscope/<slug:slug>/<slug:cat>',singCategory,name='singCategory'),
    path("openblog/",blog_list, name="blog_list"),
    path("openblog/<slug:slug>",blogDetail, name="blogDetail"),
    path('ads.txt', read_file),
    path('google2fa4526cbb5e6784.html', read_google),
    path('tag/<slug:slug>', tagged, name="tagged"),
    path("Divination-on-chamomile/",flower,name="flower"),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),

    ),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
