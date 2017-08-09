from django.conf.urls import url
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='calendar_by_user'),
    url(r'^all_events/', views.all_events, name='all_events'),
]