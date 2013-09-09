from django.conf.urls import patterns, url

from carriage import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view()),
    url(r'statistics/$',views.view_stat, name='stat'),
    url(r'^(?P<crg_id>[^/]+)/$', views.view_page,name='index'),
    url(r'^accounts/google/login/$', views.google_login, name='social_google_login'),
    url(r'^accounts/google/login/done/$', views.google_auth, name='social_google_login_done'),
)