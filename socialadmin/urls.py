from django.conf.urls import url
from . import views

app_name='socialadmin'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^kemibox/$',views.KemiBox_list.as_view(), name='kemiboxlist'),
    url(r'^kemibox/posts/$',views.Post_list.as_view(), name='postlist'),

    ]