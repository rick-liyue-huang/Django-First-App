
# coding: utf-8
from django.db import models

# Create your models here.

class Test(models.Model):
  name = models.CharField(max_length=20)

# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'rootroot666'; 
class User(models.Model):
  username = models.CharField(unique=True, max_length=50, blank=False)
  age = models.SmallIntegerField(default=0)
  phone = models.IntegerField(db_index=True, blank=True, default=0)
  email = models.EmailField(blank=True, default='')
  info = models.TextField(blank=True)
  create_time = models.DateTimeField(auto_now_add=True)
  update_time = models.DateTimeField(auto_now=True)
# 创建联合索引
  class Meta:
    index_together = ['username', 'phone']

  def __str__(self):
    return 'user: {}'.format(self.username)


# user.userprofile  因为是一对一，就相当于为user添加了新的属性userprofile
class UserProfile(models.Model):
  user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
  birthday = models.CharField(max_length=100, blank=True, default='')

  def __str__(self):
    return 'user: {}, birthday: {}'.format(self.user.username, self.birthday)

# rick.diary.values('content')  通过多对一的 related_name 相当于为user添加了diary的属性
# user = User.objects.filter(diary__id=1)  反向查询，通过diary来反向找到user
class Diary(models.Model):
  user = models.ForeignKey(User, related_name='diary', on_delete=models.SET_NULL, blank=True, null=True)
  content = models.TextField()
  create_time = models.IntegerField()

# rick.diary.values('content')  通过多对一的 related_name 相当于为user添加了diary的属性
class Group(models.Model):
  user = models.ManyToManyField(User, related_name='group')
  name = models.CharField(max_length=20)
  create_time = models.IntegerField()
  


