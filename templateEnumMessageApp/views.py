

from django.views.generic import View 
# from django.http import HttpResponse
from django.shortcuts import render
from .const import MessageType

class TemplateEnumMessage(View):

  TEMPLATE = 'message.html'

  def get(self, request, message_type):

    data = {}
    try:
      message_type_obj = MessageType[message_type]
    except Exception as e:
      data['error'] = 'no such message type {}'.format(e)
      return render(request, self.TEMPLATE, data)

    message = request.GET.get('message', '')

    if not message:
      data['error'] = 'message can not be empty'
      return render(request, self.TEMPLATE, data)

    data['message'] = message
    data['message_type'] = message_type_obj

    return render(request, self.TEMPLATE, data)

    # return HttpResponse(message)