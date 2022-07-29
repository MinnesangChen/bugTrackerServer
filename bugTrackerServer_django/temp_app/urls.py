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
    # ex: /temp_app/
    path('', views.index, name='index'),
    # ex: /temp_app/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /temp_app/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /temp_app/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]