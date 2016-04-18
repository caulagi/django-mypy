from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail1, name='detail1'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail2, name='detail2'),
]
