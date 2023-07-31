from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import TutorialSitemap

sitemaps = { 
    'blog': TutorialSitemap,
}
app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    # path('<single_slug>/', views.single_slug, name='single_slug'),
    path('<single_slug>/', views.single_slug, name='tutorial_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
     
]
