from django.conf.urls import url
from . import views


app_name = 'userProfile'
urlpatterns = [
    # user/
    url(r'^$', views.user, name="user"),
    # user/id
    url(r'^(?P<user_id>\d)/$', views.details, name="details"),
    # addUser
    url(r'^addUser', views.addUser, name="addUser")

]
