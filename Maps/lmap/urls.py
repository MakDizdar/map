from django.conf.urls import patterns, include, url
#from mapvis.views import hello
from mapvis.views import mapapp
#from mapvis.views import memb_reg
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^mapapp/$', mapapp),
    # Examples:
    # url(r'^$', 'lmap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
