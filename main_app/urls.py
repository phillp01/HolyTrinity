from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^members/([a-z0-9-]+)/$', views.detail, name="detail"),
    # url(r'^members/([a-z0-9-]+)/edit/$', views.edit, name="edit"),
    # url(r'^edit/([a-z0-9-]+)/$', views.edit, name="edit"),
    url(r'^settings/$', views.settings, name="settings"),
    url(r'^people/$', views.people, name="people"),
    url(r'^people/create/$', views.person_create, name='person_create'),
    url(r'^people/(?P<pk>\d+)/update/$', views.person_update, name='person_update'),
    url(r'^people/(?P<pk>\d+)/delete/$', views.person_delete, name='person_delete'),
]