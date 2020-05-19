
#coding: utf-8
# 定义枚举类型
from enum import Enum 

class MessageType(Enum):
  info = 'info'
  warning = 'warning'
  error = 'error'
  danger = 'danger'

MessageType.info.label = 'normal information'
MessageType.warning.label = 'warning information'
MessageType.error.label = 'error information'
MessageType.danger.label = 'danger information'

MessageType.info.color = 'green'
MessageType.warning.color = 'orange'
MessageType.error.color = 'blue'
MessageType.danger.color = 'red'

SensitiveWord = ['weather', 'bad guy', 'mood']