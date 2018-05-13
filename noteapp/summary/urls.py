from django.conf.urls import url
import .views

urlpatterns = [
    url(r'^search/$', views.SearchView.as_view(), name='search'),
]
