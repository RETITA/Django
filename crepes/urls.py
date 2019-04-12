from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'crepes.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^$', views.accueil, name='accueil'),
    url(r'^admin/', admin.site.urls),
]