#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Mosaico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^', include('Mosaico.core.urls')), #vai buscar a url na outra pasta dentro de cada aplicação, no caso "core"
    #url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
