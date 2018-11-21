"""djangotest01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from djangotest01.views import index
from django.conf import settings
from placeholder.views import placehoder,index, app, app01
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placehoder, name='placehoder'),
    url(r'^image/$', index, name="placholder"),
    url(r'^app/$', app, name="app"),
    url(r'^static/(?P<path>.*)$', views.serve),
    url(r'^app01/$',app01, name="app01")
] + staticfiles_urlpatterns() 