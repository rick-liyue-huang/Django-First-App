
# coding: utf-8

from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from .myfilter import test_filter  # 注意相对路径

def environment(**options):
  env = Environment(**options)
  env.globals.update({
    'static': staticfiles_storage.url,
    'url': reverse
  })
  env.filters['test_filter'] = test_filter
  return env

  