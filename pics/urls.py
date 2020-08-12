from django.conf.urls import url
from pics import views

app_name = 'pics'

urlpatterns = [

    url(r'^upload/$', views.UploadPage.as_view(), name='upload'),
    url(r'^user/$', views.UserPage.as_view(), name='user'),
    url(r'^profile/$', views.ProfilePage.as_view(), name='profile'),
    url(r'^profile/(?P<pk>\d+)/edit/$', views.ProfilePageUpdate.as_view(), name='edit_profile'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^dp/(?P<pk>\d+)/change/$',views.changeP.as_view(),name='dp_change')

]
