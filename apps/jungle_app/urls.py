from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views
                    

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^wall$', views.wall),
    url(r'^post$', views.post),
    url(r'^comment$', views.comment),
    url(r'^logout$', views.logout),
    url(r'^delmsg/(?P<id>[0-9]+)$', views.delmsg),
    url(r'^delcom/(?P<id>[0-9]+)$', views.delcom),
    url(r'^land$', views.land),
    url(r'^ocean$', views.ocean),
    url(r'^aerial', views.aerial),
    url(r'^food$', views.food),
    url(r'^animals$', views.animals),
    url(r'^subchannels$', views.subchannels),
    url(r'^channel_post$', views.channel_post),
  

 
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

