from django.conf.urls import url
from . import views


urlpatterns = [

    # /apli/
    url(r'^$', views.ingreso, name='ingreso'),

    # /clients
    url(r'^client/$', views.index_client, name='index_client'),
    # /client/<id>
    url(r'^client/(?P<pk>[0-9]+)/$', views.detail_client, name='detail_client'),
    # /client/new/
    url(r'^client/new/$', views.ClientCreate.as_view(), name='client_new'),
    # /client/<id>/update/
    url(r'^client/(?P<pk>[0-9]+)/update/$', views.ClientUpdate.as_view(), name='client_update'),
    # /client/<id>/delete/
    url(r'^client/(?P<pk>[0-9]+)/delete/$', views.ClientDelete.as_view(), name='client_delete'),

    # /project
    url(r'^project/$', views.index_project, name='index_project'),
    # /angebot
    url(r'^angebot/$', views.index_angebot, name='index_angebot'),
    # /aufttrag
    url(r'^aufttrag/$', views.index_aufttrag, name='index_aufttrag'),
    # /job
    url(r'^job/$', views.index_job, name='index_job'),

    # /project/<id>
    url(r'^project/(?P<pk>[0-9]+)/$', views.detail_project, name='detail_project'),
    # /project/new/
    url(r'^project/new/$', views.ProjectCreate.as_view(), name='project_new'),
    # /project/<id>/update/
    url(r'^project/(?P<pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name='project_update'),
    # /project/<id>/delete/
    url(r'^project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),

    url(r'^prueba_email/$', views.prueba_email, name='prueba_email'),
    url(r'^update/$', views.update, name='update'),
    url(r'^unsubscribe/$', views.unsubscribe, name='unsubscribe'),
    url(r'^view_prueba_email/$', views.view_prueba_email, name='view_prueba_email'),

    url(r'^busca/$', views.busca, name='busca'),                                                    # /busca/

    # /proyecto/new/ TEST proyecto
    url(r'^proyecto/new/$', views.ProjectCreate.as_view(), name='proyecto_new'),

    # /proyecto/1/update/
    url(r'^modelo/(?P<pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name='proyecto_update'),

    # /proyecto/1/delete/
    url(r'^modelo/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='proyecto_delete'),

    # /apli/models
    url(r'^model/$', views.index_model, name='index_model'),

    # /model/13
    url(r'^model/(?P<pk>[0-9]+)/$', views.detail_model, name='detail_model'),

    # /apli/projects
#    url(r'^project/$', views.index_project, name='index_project'),

    # /project/13
#    url(r'^project/(?P<pk>[0-9]+)/$', views.detail_project, name='detail_project'),

    # /apli/ isma
    url(r'^index_calendario/$', views.index_calendario, name='index_calendario'),

    # /apli/isma
    url(r'^index_cotizacion/$', views.index_cotizacion, name='index_cotizacion'),

    # /apli/isma
    url(r'^index_home_page/$', views.index_home_page, name='index_home_page'),

    # /apli/isma
    url(r'^index_orden_compra/$', views.index_orden_compra, name='index_orden_compra'),

    # /apli/isma
    url(r'^index_personas/$', views.index_personas, name='index_personas'),
]