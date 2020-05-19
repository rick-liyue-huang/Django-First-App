
from django.urls import path
from .views import TemplateEnumMessage

urlpatterns = [
  path('templateenummessage/<str:message_type>', TemplateEnumMessage.as_view(), name="three")
]