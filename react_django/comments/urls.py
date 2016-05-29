# coding: utf-8
from django.conf.urls import url

from .views import CommentsApiView

urlpatterns = [
    url('^comments/$', CommentsApiView.as_view(), name='comments')
]
