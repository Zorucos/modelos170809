from django.conf.urls import include, url
from django.contrib import admin
#from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


from apli.views import (ClienteCreateView, GeneratePDF, SubscrptionView)

urlpatterns = [
    #####esto es lo mas importnte inicio
    url(r'^admin/', admin.site.urls),
    url(r'^apli/', include('apli.urls')),
    url(r'^calendar/', include('fullcalendar.urls')),
    url(r'^register/', include('register.urls')),
    #####esto es lo ma importante fin 
	
    url(r'^apli/new-client/$', ClienteCreateView.as_view(), name ="new-client"),
	#generation PDF
	url(r'^pdf/(?P<pk>[0-9]+)/$', GeneratePDF.as_view(), name='pdf_rechnung'),
    url(r'^email/$', SubscrptionView, name="upload_pic"), # mail envio
]
