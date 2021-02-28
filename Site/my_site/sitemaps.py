from django.contrib.sitemaps import Sitemap
from .models import Blogmodel,SignsList

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return Blogmodel.objects.all()


class SingSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return SignsList.objects.all()

    

