from django.conf.urls import url, include
from . import views
from . import views as core_views
from django.contrib.auth import views as auth_views

app_name = 'schoolnow'

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<mensagem_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^bemvindo/$', views.bemvindo, name='bemvindo'),
   
    url(r'^criarmemorando/$', views.criarmemorando, name='criarmemorando'),
    url(r'^memorias/$', views.memorias, name='memorias'),
    #url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.password_reset_confirm, {'template_name': 'password_reset_confirm.html', 'post_change_redirect': 'schoolnow:password_reset_confirm'}, name='password_reset_confirm'),
    #url(r'^reset/$', views.reset, name='reset'),
    #url(r'^songs/$', views.songs, name='songs'),
    #url(r'^reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', views.password_reset_confirm, name='password_reset_confirm'),
    #url(r'^reset/$', views.reset, name='reset'),

    #url(r'^accounts/login/$')

        
]

    #url(r'^register/$', core_views.register, name='register'),
    #url(r'^criarmemorado/$', views.update_profile, name='criarmemorado'),
