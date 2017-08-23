from django.conf.urls import patterns, include, url

from django.contrib.auth.views import login, logout

urlpatterns = patterns('Mosaico.core.views',
    # Examples:
    # url(r'^$', 'Mosaico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'home', name='home'),
	url(r'^contato/$', 'contato', name='contato'),
	# Login/Logout URLs
	url(r'^login/$', 'login', name='login'),
	#url(r'^logout/$', 'logout', name='logout'),

	#url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	#url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/login/'}),

)
