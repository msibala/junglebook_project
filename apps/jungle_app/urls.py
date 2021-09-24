from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views
                    

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^land$', views.land),
    url(r'^ocean$', views.ocean),
    url(r'^wing$', views.wing),
 
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

