from django.conf.urls import url
from store import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^favorites/$', views.favorites, name="favorites"),
    url(r'^register/$', views.register, name="register"),
    url(r'^createproduct/$', views.createproduct, name="createproduct"),
    url(r'^productview/(?P<pk>\d+)/$', views.productview, name='productview'),
    url(r'^productlist/(?P<category>.+)/(?P<producer>.+)*/$', views.productlist, name="productlist"),
    url(r'^(?P<url>.+)/$', views.like, name="like")
]
