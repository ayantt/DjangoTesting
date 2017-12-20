from django.conf.urls import include, url
from django.contrib import admin

app_name = 'helloWorld'
urlpatterns = [
    #url(r'^$',)
    #url(r'^addUser', include('addUser.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('hello.urls')),
    url(r'^users/', include('userProfile.urls')),
    
]
