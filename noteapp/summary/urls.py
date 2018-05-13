from django.conf.urls import url
from summary import views

urlpatterns = [
    url(r'^search/$', views.SearchView.as_view(), name='search'),
]
