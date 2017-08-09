from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


from apli.views import (ClienteCreateView, RegisterView, GeneratePDF, SubscrptionView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^apli/', include('apli.urls')),
    url(r'^calendar/', include('fullcalendar.urls')),

    #url log in out register
    url(r'^login/$', auth_views.LoginView.as_view(template_name='apli/login.html'), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='apli/logout.html'), name="logout"),
    url(r'^register/$', RegisterView.as_view(template_name='apli/register.html'), name="register"),

    #url para resset password
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
	url(r'^admin/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	url(r'^apli/new-client/$', ClienteCreateView.as_view(), name ="new-client"),

	#generation PDF
	url(r'^pdf/(?P<pk>[0-9]+)/$', GeneratePDF.as_view(), name='pdf_rechnung'),

    url(r'^email/$', SubscrptionView, name="upload_pic"), # mail envio
]
