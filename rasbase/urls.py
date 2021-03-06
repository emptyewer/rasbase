"""Rasbase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

import home.views as home
import dashboard.views as dashboard
import search.views as search
import upload.views as upload

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.index, name='index'),
    url(r'^about', home.about, name='rasbase-about'),
    url(r'^dashboard', dashboard.dashboard, name='rasbase-dashboard'),
    url(r'^search', search.search, name='rasbase-search'),
    url(r'^results', search.search, name='rasbase-results'),
    url(r'^upload', upload.UploadView.as_view(), name='rasbase-upload'),
    url(r'^messages', upload.PendingView.as_view(), name='rasbase-messages'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

