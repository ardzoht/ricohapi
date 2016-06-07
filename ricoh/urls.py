from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api.views import PrinterLog, Printers, Dashboard, Connection, Log

router = routers.DefaultRouter()
router.register('printers', Printers)
router.register('logs', PrinterLog)
urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'ricoh.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', Dashboard.as_view(), name='dashboard'),
    url(r'^log/', Log.as_view(), name='log'),
    url(r'^dashboard/connection', Connection.as_view(), name='connection'),
    url(r'^api/', include(router.urls))
)
