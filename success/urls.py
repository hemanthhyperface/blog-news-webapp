
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import logout, urls
from django.contrib.auth import authenticate, login
from django.urls import path
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
  

]
