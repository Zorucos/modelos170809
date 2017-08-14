from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.ingreso, name='ingreso'),                                                      # /apli/

    url(r'^client/$', views.index_contact, name='index_contact'),                                   # /clients
    url(r'^client/(?P<pk>[0-9]+)/$', views.detail_contact, name='detail_contact'),                  # /client/<id>
    url(r'^client/new/$', views.ClientCreate.as_view(), name='client_new'),                         # /client/new/
    url(r'^client/(?P<pk>[0-9]+)/update/$', views.ClientUpdate.as_view(), name='client_update'),    # /client/<id>/update/
    url(r'^client/(?P<pk>[0-9]+)/delete/$', views.ClientDelete.as_view(), name='client_delete'),    # /client/<id>/delete/

    url(r'^busca/$', views.busca, name='busca'),                                                    # /busca/
                                                       #task

    # /proyecto/new/ TEST proyecto
    url(r'^proyecto/new/$', views.ProyectoCreate.as_view(), name='proyecto_new'),

    # /proyecto/1/update/
    url(r'^modelo/(?P<pk>[0-9]+)/update/$', views.ProyectoUpdate.as_view(), name='proyecto_update'),

    # /proyecto/1/delete/
    url(r'^modelo/(?P<pk>[0-9]+)/delete/$', views.ProyectoDelete.as_view(), name='proyecto_delete'),

    # /apli/models
    url(r'^model/$', views.index_model, name='index_model'),

    # /model/13
    url(r'^model/(?P<pk>[0-9]+)/$', views.detail_model, name='detail_model'),


    # /apli/projects
    url(r'^project/$', views.index_project, name='index_project'),

    

    # /project/13
    url(r'^project/(?P<pk>[0-9]+)/$', views.detail_project, name='detail_project'),

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

         # /apli/isma
    url(r'^index_contact/$', views.index_contact, name='index_contact'),

]