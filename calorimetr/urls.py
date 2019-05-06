from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BaseView, name='base'),
    url(r'^signup/$', views.SignupView, name='signup'),
    url(r'^diary/$', views.IndexView, name='diary'),
    url(r'^diary/search/(?P<eating_id>[0-9]+)/$', views.SearchView, name='search'),
    url(r'^diary/search/(?P<eating_id>[0-9]+)/add/$', views.add, name='add'),
    url(r'^diary/(?P<eating_id>[0-9]+)/delete/$', views.del_dish, name='delete'),
    url(r'^rsk/$', views.RSKView, name='rsk'),
    url(r'^weight/$', views.WeightView, name='weight'),
    url(r'^calendar/$', views.CalendarView, name='calendar'),
    #url(r'^diary/search/searching/$', views.SearchView.as_view(), name='searching'),
]
