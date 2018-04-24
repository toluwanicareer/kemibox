from django.conf.urls import url
from . import views

app_name='socialadmin'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^kemibox_ajax/$',views.KemiBox_list.as_view(), name='kemiboxlist_ajax'),
    url(r'^kemibox_ajax/posts/$',views.Post_list.as_view(), name='postlist'),
    #url(r')
    ]