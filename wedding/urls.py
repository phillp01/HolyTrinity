from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^weddings/$', views.weddings, name="weddings"),
    url(r'^wedding/create/$', views.wedding_create, name='wedding_create'),
    url(r'^weddings/(?P<pk>\d+)/update$', views.wedding_update, name="wedding_update"),
    url(r'^weddings/(?P<pk>\d+)/delete$', views.wedding_delete, name="wedding_delete"),

    url(r'^readings/(?P<pk>\d+)/create$', views.reading_create, name="reading_create"),
    url(r'^readings/(?P<pk>\d+)/update$', views.reading_update, name="reading_update"),
    url(r'^readings/(?P<pk>\d+)/delete$', views.reading_delete, name="reading_delete"),


    url(r'^hymns/(?P<pk>\d+)/create$', views.hymn_create, name="hymn_create"),
    url(r'^hymns/(?P<pk>\d+)/update$', views.hymn_update, name="hymn_update"),
    url(r'^hymns/(?P<pk>\d+)/delete$', views.hymn_delete, name="hymn_delete"),

    url(r'^people/(?P<pk>\d+)/create/$', views.person_create, name='person_create'),
	url(r'^ajax/autocomplete/$', views.autocomplete, name='ajax_autocomplete')
]

urlpatterns += [
    url('total_wedding_amount/', views.total_wedding_amount, name='total_wedding_amount'),
]

urlpatterns += [
    url('brideandgroomdetails/', views.brideandgroomdetails, name='brideandgroomdetails'),
	url('auto_update_wedding_id/', views.auto_update_wedding_id, name='auto_update_wedding_id'),
	url('brideandgroomdetails2/', views.brideandgroomdetails2, name='brideandgroomdetails2'),
	url('auto_update_wedding_id2/', views.auto_update_wedding_id2, name='auto_update_wedding_id2'),
]

urlpatterns += [
	 url('get_bride_groom_id/', views.get_bride_groom_id, name='get_bride_groom_id'),    
	 url('groomDetails/', views.groomDetails, name='groomDetails'),
     url('brideDetails/', views.brideDetails, name='brideDetails'),
     url('get_church/', views.get_church, name='get_church'),
]