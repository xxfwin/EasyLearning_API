from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getSimilarCourses$', views.getSimilarCourses, name='getSimilarCourses'),
    url(r'^updateCourses$', views.updateCourses, name='updateCourses'),
]
