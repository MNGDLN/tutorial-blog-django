from django.contrib.sitemaps import Sitemap
from .models import Tutorial


class TutorialSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Tutorial.objects.filter(status="PB").order_by('-tutorial_published')

    def lastmod(self, obj):
        return obj.tutorial_published