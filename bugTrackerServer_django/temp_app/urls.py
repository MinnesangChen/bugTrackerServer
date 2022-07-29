# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/26 16:07
@Author  : JW Chen
@File    : urls.py

"""
# from django.conf.urls import url
#
# from . import views
#
# urlpatterns = [
#     url(r'^$', views.hello),
# ]

from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]