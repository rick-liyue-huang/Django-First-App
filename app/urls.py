
# coding: utf-8

from django.urls import path
# from .views import TestOne
from .views import Index


urlpatterns = [
    path('<str:name>', Index.as_view(), name='index')
]

# urlpatterns = [
#     path('testone/<str:message>', TestOne.as_view(), name='testOne')
# ]


'''
# coding: utf-8
# from django.conf.urls import url
# same as from django.urls import path
from django.urls import path
# from .views import index
from .views import Index

# method 1: ?
# urlpatterns = [
#     url('index/', index)
# ]

# method 2: /arg/arg
urlpatterns = [
    path('index/<str:name>/<str:gender>', Index.as_view())
]
'''
