from django.conf.urls import patterns, include, url

urlpatterns = patterns('Mosaico.core.views',
    # Examples:
    # url(r'^$', 'Mosaico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'home', name='home'),
	url(r'^contato/$', 'contato', name='contato'),
)
