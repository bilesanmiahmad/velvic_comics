from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^titles/$', views.post_titles_list, name='post_titles'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
