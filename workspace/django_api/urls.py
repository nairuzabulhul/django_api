from django.conf.urls import url, include
from django_api import views

urlpatterns = [
    
    url('^books/?$', views.BookList.as_view()),
    url('^books/(?P<pk>[0-9]+)/?$', views.BookDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
