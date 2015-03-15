from django.conf.urls import patterns, url

from auth_module import views

urlpatterns = patterns('',
	url(r'^login/$', views.login_action, name='login'),
	url(r'^$', views.login_action, name='index'),
	url(r'^registration/$', views.registration, name='registration'),
	url(r'^logout/$', views.log_out_action, name='logout'),
)