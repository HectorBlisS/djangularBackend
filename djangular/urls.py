from django.conf.urls import url, include
from django.contrib import admin
from scrumboard import urls as scrumUrls
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scrumboard/',
    	include(scrumUrls)),
    url(r'^$',
		TemplateView.as_view(template_name="scrumboard/home.html")),
]
