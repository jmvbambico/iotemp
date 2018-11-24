from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^thermo/', include('thermo.urls')),
    url(r'^admin/', admin.site.urls),
]