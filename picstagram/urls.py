"""picstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from pics import views

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'', include('pics.urls', namespace='pics')),
                  url(r'^$', auth_views.LoginView.as_view(template_name='pics/login_signup_page.html'), name='login'),
                  url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
                  url(r'^home/$', views.HomePage.as_view(), name='home'),
                  url(r'^signup/$', views.SignUp.as_view(), name='signup'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
