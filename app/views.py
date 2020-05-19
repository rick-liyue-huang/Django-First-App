
# creating views here

# coding: utf-8

from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
import datetime


class Index(View):
    TEMPLATE = 'index.html'  # 因为已经在setting中注册过了，所以直接使用

    def get(self, request, name):

        # 定义参数
        data = {}
        data['name'] = name
        data['array'] = range(2, 22, 2)  # [] is empty
        data['count'] = 20
        data['time'] = datetime.datetime.now()
        data['cut_str'] = 'hello world'
        data['first_big'] = 'hello django'
        data['result'] = False
        data['result1'] = None
        data['dict_list'] = [{'name': 'rick', 'age': 18},
                             {'name': 'leo', 'age': 22}]
        data['float_num'] = 3.14159
        data['html_str'] = '<div style ="background-color:red;width:50px;height:50px"> 123 < /div >'
        data['a_str'] = 'please www.baidu.com'
        data['future'] = data['time'] + datetime.timedelta(days=5)
        return render(request, self.TEMPLATE, data)


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
