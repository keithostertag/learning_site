from django.conf.urls import url

from . import views

# remember... the order is important since it searches top to bottom!
urlpatterns = [
    url(r'^$', views.course_list),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail),
    url(r'(?P<pk>\d+)/$', views.course_detail),
]
