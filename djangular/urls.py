from django.conf.urls import url, include
from django.contrib import admin
from scrumboard import urls as scrumUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scrumboard/',
    	include(scrumUrls)),
]
