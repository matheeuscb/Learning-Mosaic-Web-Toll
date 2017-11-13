from django.conf.urls import patterns, include, url

from django.contrib.auth.views import login, logout

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('Mosaico.core.views',
    # Examples:
    # url(r'^$', 'Mosaico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'home', name='home'),
	#url(r'^contato/$', 'contato', name='contato'),
	url(r'^login/$', 'login', name='login'),
	url(r'^dashboard/$', 'dashboard', name='dashboard'),
	url(r'^logout/$', 'logout', name='logout'),
	#url(r'^sobre/$', 'sobre', name='sobre'),
	url(r'^teste/$', 'teste', name='teste'),
	#url(r'lgteste/$', 'lgteste', name='lgteste'),
	url(r'dashboard/criar_canvas.html/$', 'criar_canvas', name='criar_canvas'),
	url(r'dashboard/inicio_dashboard.html/$', 'inicio_dashboard', name='inicio_dashboard'),
	url(r'dashboard/listagem_canvas.html/$', 'listagem_canvas', name='listagem_canvas'),
	url(r'dashboard/listagem_areas.html/(?P<id_canvas>[0-9]+)$', 'listagem_areas', name='listagem_areas'),
	url(r'dashboard/editar_area.html/(?P<id_area>[0-9]+)$', 'editar_area', name='editar_area'),
	url(r'dashboard/criar_area.html/(?P<id_canvas>[0-9]+)$', 'criar_area', name='criar_area'),
	url(r'dashboard/excluir_area.html/(?P<id_area>[0-9]+)$', 'excluir_area', name='excluir_area'),
	url(r'dashboard/editar_canvas.html/(?P<id_canvas>[0-9]+)$', 'editar_canvas', name='editar_canvas'),
	url(r'dashboard/excluir_canvas.html/(?P<id_canvas>[0-9]+)$', 'excluir_canvas', name='excluir_canvas'),
	url(r'dashboard/listagem_mosaicos.html/$', 'listagem_mosaicos', name='listagem_mosaicos'),
	url(r'dashboard/criar_mosaico.html/$', 'criar_mosaico', name='criar_mosaico'),
	url(r'dashboard/listagem_objetivos.html/(?P<id_canvas>[0-9]+)$', 'listagem_objetivos', name='listagem_objetivos'),
	url(r'dashboard/listagem_murais.html/(?P<id_canvas>[0-9]+)$', 'listagem_murais', name='listagem_murais'),
	url(r'dashboard/criar_objetivo.html/(?P<id_mosaico>[0-9]+)$', 'criar_objetivo', name='criar_objetivo'),
	url(r'dashboard/editar_objetivo.html/(?P<id_objetivo>[0-9]+)$', 'editar_objetivo', name='editar_objetivo'),
	url(r'dashboard/excluir_objetivo.html/(?P<id_objetivo>[0-9]+)$', 'excluir_objetivo', name='excluir_objetivo'),
	url(r'registro/$', 'registro', name='registro'),
	url(r'perfil/$', 'perfil', name='perfil'),
	url(r'dashboard/relatorio_canvas.html/$', 'relatorio_canvas', name='relatorio_canvas'),
	url(r'dashboard/relatorios.html/$', 'relatorios', name='relatorios'),
	url(r'dashboard/grafico3$', 'grafico3', name='grafico3'),
	url(r'dashboard/listagem_graficos.html/(?P<id_canvas>[0-9]+)$', 'listagem_graficos', name='listagem_graficos'),
	url(r'dashboard/grafico_status_final.html/(?P<id_canvas>[0-9]+)$', 'grafico_status_final', name='grafico_status_final'),
	url(r'dashboard/grafico_status_inicial.html/(?P<id_canvas>[0-9]+)$', 'grafico_status_inicial', name='grafico_status_inicial'),
	url(r'dashboard/grafico_dimensao.html/(?P<id_canvas>[0-9]+)$', 'grafico_dimensao', name='grafico_dimensao'),
	url(r'dashboard/mural/(?P<id_canvas>[0-9]+)/(?P<id_user>[0-9]+)$', 'mural', name='mural'),
	#url(r'dashboard/pegar_verbo.html/$', 'pegar_verbo', name='pegar_verbo'),
	url(r'dashboard/pegar_areas.html/$', 'pegar_areas', name='pegar_areas'),
	#url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	#url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/login/'}),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
