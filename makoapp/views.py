
# coding: utf-8

from django.views.generic import View
from .base_render import render_to_response

class Test(View):
  TEMPLATE = 'test.html'

  def get(self, request):

    data = {'name': 'rick', 'age': 19}
    return render_to_response(request, self.TEMPLATE, content=data)
