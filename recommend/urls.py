from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getRecommendCourses$', views.getRecommendCourses, name='getRecommendCourses'),
    url(r'^updateRecommendCourses$', views.updateRecommendCourses, name='updateRecommendCourses'),
]
