
# coding: utf-8

from mako.lookup import TemplateLookup
from django.template import RequestContext
from django.conf import settings
from django.template.context import Context
from django.http import HttpResponse


def render_to_response(request, template, content=None):
  context_instance = RequestContext(request)
  path = settings.TEMPLATES[0]['DIRS'][0]  # 找到对应的setting 配置
  lookup = TemplateLookup(
    directories = [path],
    output_encoding = 'utf-8',
    input_encoding = 'utf-8'
  )
  mako_template = lookup.get_template(template)

  if not content:
    content = {}

  if context_instance:
    context_instance.update(content)
  else:
    context_instance = Context(content)

  result = {}

  for d in context_instance:
    result.update(d)

  result['csrf_token'] = '<input type="hidden" name="csrfmiddlewaretoken" value="{0}" />'.format(request.META.get('CSRF_COOKIE',""))
  return HttpResponse(mako_template.render(**result))