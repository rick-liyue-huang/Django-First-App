
# creating views here

# coding: utf-8

from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse


class Index(View):
    TEMPLATE = 'index.html'

    def get(self, request, gender):
        return render(request, self.TEMPLATE, {'name': 'rick', 'gender': gender})


'''
class TestOne(View):
    def get(self, request):
        message = request.GET.get('message', 'no content')
        return HttpResponse(message)
'''


# class TestOne(View):

#     def get(self, request, message):
#         return HttpResponse(message)


'''
# coding: utf-8

from django.http import HttpResponse
from django.views.generic import View

# method 1:
# def index(request):
#     name = request.GET.get('name', '')
#     gender = request.GET.get('gender', '')

#     # return HttpResponse('hello django2')
#     return HttpResponse("Hi, I'm {}, and I'm {}".format(name, gender))

# method 2:
# def index(request, name, gender):
#     return HttpResponse("Hi, I'm {}, and I'm {}".format(name, gender))


# 引入视图类
class Index(View):
    def get(self, request, name, gender):
        print(dir(request))
        return HttpResponse("Hi, I'm {}, and I'm {}".format(name, gender))
'''
