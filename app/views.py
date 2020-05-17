
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
