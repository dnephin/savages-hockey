from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^hockey_register/', include('hockey_register.foo.urls')),

	(r'^login$', 'django.contrib.auth.views.login'),
	(r'^logout$', 'django.contrib.auth.views.logout'),
	(r'^$', 'hockey_register.register.views.index'),
	(r'^update_status$', 'hockey_register.register.views.update_status'),
	(r'^status/(?P<game_day>\d{4}-\d{2}-\d{2})$', 'hockey_register.register.views.status'),
	(r'^status/$', 'hockey_register.register.views.status'),


	

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
