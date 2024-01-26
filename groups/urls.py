#GROUPS URLS.PY

from django.urls import re_path, include
from . import views
from django.conf import settings

app_name = 'groups'

urlpatterns = [
    re_path(r'^$',views.ListGroups.as_view(),name='all'),
    re_path(r'^new/$',views.CreateGroup.as_view(),name='create'),
    re_path(r'^posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
    re_path(r'^join/(?P<slug>[-\w]+)/$',views.JoinGroup.as_view(),name='join'),
    re_path(r'^leave/(?P<slug>[-\w]+)/$',views.LeaveGroup.as_view(),name='leave')
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns
