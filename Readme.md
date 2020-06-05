## First Project in Django2

### 项目介绍

该项目是一个简单的消息发布和获取练习，该项目围绕 Django2 的基础课程，对项目进行更新，本项目以练习 Django 基础为主，并不涉及太多的复杂操作，如消息订阅和发布，socket 长连接等。

### 路由器和视图 urls and views

#### 路由器

1. 简单地说，url 就是常说的网址，每个网址代表不同的网页
2. 在 Django 中 url 也称为 urlconf
3. 每个 url 地址对应一个唯一的 views 视图函数
4. 根目录项目中的 urls.py 是根路由，根路由可以集合所有的应用路由
5. 每个应用下创建自己的 urls.py, 这个 urls.py 属于每个应用的独立路由，通过继承或者说绑定到根路由中进行使用
6. 路由常用方法，变量和 views 的绑定

```
from django.urls import path, include  # 导入 url 模块
from django.contrib import admin # 导入 admin 功能模块
urlpatterns = [
    path('admin/', admin.site.urls),
]  # 整个项目的 url 集合，每个元素代表一条 url 信息
# path('admin/', admin.site.urls) 设置 admin 的 url
# admin/ 代表 url 地址 即： http://127.0.0.1:8000/admin, admin 后边的斜杠为路径的分隔符，
# admin.site.urls 是对应的视图函数

path('', include('app.urls))
# 如果 url 为空即代表为网站的域名，即 127.0.0.1:8000, 通常为网站的首页，include是将应用 app 中的 urls 包含进来

# 另外一种写法
from app import urls as app_urls
path('', include(app_urls))

# 这里需要注意：网址分两部分， domain域名与url按照上边的地址分别是127.0.0.1 和 admin

```

#### 视图

views 是 Django 的 mvt 中的 v 部分，主要是负责处理用户的请求和生成相应的内容，然后在页面或者其他类型文档中显示

```
from django.http import HttpResponse

def index(request):
  return HttpResponse('hello django')

```

#### url 中的参数的两种形式

1. 在 url 后边用?开始，键与值用等号连接，每对键值用&区分，如: http://127.0.0.1:8000/app?name=rick&gender=male
2. 在路由的参数中用分隔符分开，如: http://127.0.0.1:8000/app/rick/male
3. 字符串类型：匹配任何非空字符串，但不包含/，在不指定类型的前提下，默认字符串类型 <str:name>
4. 整形：匹配 0 和正整数 <int:age>
5. slug：理解为注释，后缀或复数等概念 <slug:day>
6. uuid：匹配一个 uuid 格式的对象 <uuid:uid> 类似 xxx-xx-xx

```
from django.urls import path # django 2.0 以后的新方法
from django.conf.url # 之前的方法，不支持参数中的类型，只能通过正则表达式的方式进行基本的匹配
path('app', view_function, name='app')
# 别名可以在重定向和模板定义的时候直接用别名代替，具体使用方法...
```

7. 视图的读取参数: ?形式的参数 -> request.GET.get(参数名)
8. 以分隔符形式的参数: def index(request, 参数名 1，参数名 2): print(参数名)

notice python38_env 虚拟环境

#### 视图分析：将视图分为三个部分

1. 用户的请求 request
2. 对用户请求的逻辑处理 handle
3. 将处理后的数据返回给用户 response
4. request 是浏览器向服务器发送的请求对象，包含用户信息，请求内容和请求方法， 可以用 dir(request) 查看 request 对象的所有方法

```
request.GET -> 获取url ? 形式的参数
request.POST -> 获取post提交的数据
request.path -> 请求的路径，比如请求 127.0.0.1/test/1 那这个值就是 /test/1
request.method -> 请求的方法 get or post
request.COOKIES -> 请求过来的cookies
request.user -> 请求的用户对象，可以通过它判断用户是否登录，并获取用户信息
request.session -> 一个既可以读也可以写的类似于字典的对象，表示当前的对话
request.META -> 一个标准的python字典，包含所有的HTTP首部信息。具体的的头部信息取决于客户端和服务器

```

5. HttpResponse 可以直接返回一些字符串内容
6. render 将数据在模板中渲染并显示
7. JsonResponse 返回一个 json 类型，通常用于与前端进行 ajax 交互

```
from django.http import HttpResponse
from django.shorcuts import render
from django.http import JsonResponse
```

8. 视图面向对象的写法

```
from django.views.generic import View
class Test(View):
  def get(self, request):
    pass
```

9. restful 规范和 HTTP 协议：Url 定位资源，简单来说，通过一个 URL 地址可以让我们知道这个地址索要提供的功能是什么，比如说 127.0.0.1/add/user 那么可以看出我么这个 URL 要做的事情就是添加一个用户，再比如 127.0.0.1/get/user/1 就可以很轻松的读出来是为了获取一个用户并且这个用户 id 是 1，总之 URL 一切皆资源。
10. Get 获取资源的时候使用，比如我们查看一个网页，Post 提交资源的时候使用，比如我么注册一个用户的时候，Put 修改资源的时候，比如我么修改自己的用户信息，Delete 删除资源的时候使用，比如我么注销我们的账号的时候。
11. HTTP 是无状态的，当浏览器发送请求给服务器的时候，服务器响应客户端请求，但是当同一个浏览器再次发给服务器发送请求的时候，服务器并不知奥它就是刚才那个浏览器，简单的说服务器不记得浏览器所以就是无状态的。
12. 200 成功， 400 请求错误，一般是参数格式有错误，403 禁止访问，404 没有获取到 URL 地址， 405 方法禁用，比如这个地址指定用 get 方法，但是使用了 post 方法， 500 服务器异常

### Template 模板

模板可以动态生成 HTML 网页，它包括部分 HTML 代码和一些特殊的语法。一般 template 模板存放在'templae'目录中，通过在项目 Settings 的 templates 的 DIRS 列表中添加对应的路径即可，如 `os.path.join(BASE_DIR, 'template')` 。 通过 `from django.shorcuts import render` 模块，`return render(request, template_path, {k:v})` 字典中的 key 和 value 就是要向前端渲染出的数据。在 HTML 中以{{}} 为标识，在{{}}中传入视图中的数据就可以了。

#### Template 内置标签和静态文件配置

1. 变量用 {{}} 包裹，比如我么后端渲染过来的数据，用 {{name}}
2. 内置标签类型，用 {% %}

```
{% for %} {% endfor %}   # 遍历输出内容
{% if %} {% elif %} {% endif %}  # 对变量条件判断
{% url name args %} # 引用路由配置名
{% load %} # 加载 django标签库
{% load static %}
{% static static_path %}  # 读取静态资源
{% extends base_template %} # 模板继承
{% block data %} {% endblock %} # 重写父模板代码
{% csrf_token %} # 跨域的密钥
```

3. for 标签模板

```
forloop.counter # 从1开始计算获取当前的索引
forloop.counter0 # 从0开始计算获取当前的索引
forloop.revcounter # 索引从最大到1
forloop.revcounter0 # 搜因从最大到0
forloop.first # 当前元素是否是第一个
forloop.last # 当前元素是否是最后一个
empty # 为空的情况
```

4. 静态文件的配置是：项目根目录创建 'static' 与 'template' 同级，`STATICFILES_DIRS=(os.path.join(BASE_DIR), 'static',)`，静态文件包括 css 文件，JS 文件，Image 文件
5. 在实际的开发中可以使用'base.html'作为基础模板来处理整个布局以及使用 block 来空出来要添加的信息，然后让其他的模板通过`{% extends 'base.html' %}`来继承这个模板.并且在相应的位置添加实际的代码，这里需要保持 block 名称的一致。

#### 模板内置过滤器

1. 用于在 HTML 模板中，对于渲染过来的数据进行二次操作使用，过滤器其实就是用来处理这些数据的模板引擎中使用的函数。也就是在前端使用 Python 的语言，就需要有过滤器。

```
# 常用的过滤器介绍
add {{value|add"10}} # value 加10
date {{value|date:"Y-m-d H:i:s"}} # 把日期格式按照规定的形式显示
cut {{value|cut:'xx'}} # 删掉 value中的xx
capfirst {{value|capfirst}} # value首字母大写
default {{value|default:'xx'}} # 值为false时候使用默认值
default_if_none {{value|default_if_none:'xx'}} 值为空时候使用默认值
dictsort {{value|dictsort:'key'}} # 值为字典的列表，按照key排序
dictsortreversed {{value|dictsortreversed:'key'}} # 上边方法反序
frist {{value|first}} # 返回列表中的第一个索引值
floatformat {{value|floatvalue:2}} # 保留小数点2位
join {{value|join:'xx'}} # 类似于 'xx'.join(value)
last {{value|last}} # 返回列表的最后索引值
length {{value|length}} # 返回值的长度
divisibleby {{value|divisibleby:2}} # 如果可以被2整除就返回true
length_is {{value|length_is:'2'}} # 如果长度是2就返回true
safe {{value|safe}} # 将字符串中的html在前端安全显示
random {{value|random}} # 随机列表中的一个值
slice {{value|slice:'2'}} # 截取前两个字符
slugify {{value|slugify}} # 值小写，单词用-分割
upper {{value|upper}} # 字符串大写
urlize {{value|urlize}} # 字符串中连接可点击
wordcount {{value|wordcount}} # 字符串中单词数目
timeuntil {{value|timeuntil}} # 距离当前日期的天数和小时数
```

2. 自定义过滤函数：在 Django 服务器端编写函数，在模板中可以直接调用过滤器函数，在应用下创建 templatetags 文件夹，在文件夹下创建 myfilter.py 文件

```
from django import template
register = template.Library() # 定义过滤器
@register.filter
def test_filter(value, args):
  return value + args

{% load myfilter %}
{{data|test_filter:3}}
```
3. Jinja2 是一套模仿Django模板的模板引擎，由Flask开发，提倡html和Python开发工作分离。
4. Mako 模板可以在HTML中随意书写Python代码
5. 需要单独在setting.py中配置jinja2的模板配置环境。同时不需要 `{% load static %} {% load my_filter %}` 因为已经在base.py中配置了 'myfilter'。
6. 对于mako需要在应用中配置 'base_render.py'来处理模板的的设置


### Model 数据

#### ORM

1. ORM 全称是 object relational mapping, 通过使用它，我们可以直接使用python的方法使用数据库，通过把表映射为类，把行作为实例，把字段多为属性，orm在执行对象操作的时候会把对应的操作转换为数据库源生语句的方式来执行完成数据库的开发工作。orm使用简单，通过将数据库语法进行封装，直接使用方法即可以操作数据库，性能好，在通过orm转换为SQL的时候是会有一些消耗，但是这个消耗其实非常低，在对整个业务提升的角度来说，这点消耗可以忽略不计，除非对IO的消耗非常极端，兼容性好，支持目前市面上多数的关系型数据库，如MYSQL。
2. Django中的虚拟对象数据库也叫模型，通过模型实现对目标数据库的读写进行操作，实现如下：在setting.py中设置数据库信息（需提前在数据库中创建库）；在应用app的models.py中以类的形式定义模型；通过模型在目标数据库中建立对应的表；在视图函数中通过对模型的操作实现目标数据库的读写操作。

```
# 在 settings.py中设置数据库配置
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'blog',  # 数据库名称
    'USER': 'root', # 数据库用户名
    'PASSWORD': '', # 数据库密码
    'HOST': '', # 数据库主机 默认为 localhost
    'PORT': '3306'  # 数据库端口
  }
}
```


```
# models.py in modelApp.py
from django.db import models

class Test(models.Model):
  name = models.CharField(max_length=20) # 创建列！！！
```

3. 同步数据库，需要 `python manage.py makemigrations`, 在migrate文件夹下生成 initial.py脚本文件；`python manage.py migrate` 将initial.py脚本中的代码执行，生成相对应的数据表。然后执行 `desc modelApp_test` 查看其中的列表

```
create database trymodel
;
use trymodel;
show tables;
```

4. Model 列方法与属性：来自于models对象; 包括CharField, TextField, EmailField,  UrlField, BooleanField, NullField, IntegerField, SmallIntegerField, BigIntegerField, PositiveIntegerField, PositiveSmallIntegerField, FloatField, DecimalField, DateField, DateTimeField, TimeField, ImageField, FileField; 特殊类型属性包括: max_digits, decimal_places, width_field, height_field, upload_to, 公共属性包括: null, blank, primary_key, auto_now, auto_now_add, max_length, default, verbose_name, db_column, unique, db_index; 表关联包括 字段名：ForeignKey,(一对多), OneToOneField(一对一), ManyToManyField(多对多), 属性名: related_name(关联表的名称), on_delete(外键删除对策)
```
from django.db import models
models.CharField...
dir(models)
```

5. 数据库的表关系以及联合索引的创建
5.1.1. 一对一: 仅在两个表中，表1的a这一行的数据和表2的a的这行数据有关系，且表2的a行数据也只会和表1的a行有关系。也就是两个表中的各有一行之间有关系。
5.1.2. 一对多: 表1的第a行数据和多个表的多行数据都会有所关系，而 多个表中都有行数据与表1的第a行有所关系，且只和表1的a行有关系。
5.1.3. 多对多：表1的第a行数据可与表2中的一行或者多行相互联系，表2中的a行也可以与表1中的一行或者多行相互联系。
5.1.4. 联合索引就是一个表中有两个字段需要合并使用一个索引
```
class meta:  # 联合索引的创建方法
  unique_together = ['day', 'hour']
  index_together = ['username', 'phone']
```

#### 数据库的增删改查

在数据库创建好后，需要对数据库进行操作。

1. 创建方法

```
User.objects.create(xx=xx, xx=xx) # method one
user = User(xx=xx, xx=xx) user.save() # method two
User.objects.get_or_create(xx=xx, xx=xx) # method three
user = User() user.xx = xx user.save() # method four
```

2. 简单的查询方法

```
user = User.objects.get(id=xx)
Users = User.objects.all()
# 可以使用 vars() 方法将user 变为字典形式
```

3. 更新方法

```
User.object.update(xx=xx, xx=xx) # mehtod one
user.xx = xx # method two
user = User.objects.filter(id=xx)
```

4. 删除方法

```
user = User.objects.get(id=xx)
user.delete()
```

5. ORM 的两种查询模式

```
User.objects.raw('select * from user')  # 原生的sql查询方法
User.objects.filter(id=xx)  # 基于orm的方法 
User.objects.all() # 返回user表中所有数据
User.objects.get(**filter) # 返回过滤条件的数据,单调
User.objects.all()/filter.exists() # 返回是否有对象
User.objects.all()/filter().count() # 返回获取的对象的数量
User.objects.all()/filter().exclude(**filter) # 返回的数据排除满足**filter的
User.objects.filter().distinct('age) # 返回的对象中通过某个列去重
User.objects.filter().order_by('age') # 返回的对象中通过age排序
dir(User.objects) # 还有更多可能不太常用的方法
# 注意 上面的链式操作不一定依赖一级方法
```
深入查询
```
__exact, __iexact, __contains, __icontains, __gt, __gte, __lt, __lte, __isnull
__startswith, __istartswith, __endswith, __iendswith, __in
```

6. Q 或查询

```
from django.db import Q
user = User.objects.filter(Q(username='rick') | Q(username='rick'))
```

7. 聚合查询 存在于 `from django.db.models import Avg, Count, Sum, Max, Min`

```
Avg 平均值 User.objects.all().aggregate(Avg='age')
Sum 取和 User.objects.all().aggregate(Sum='age')
Max 最大值 User.objects.all().aggregate(Max='age')
Min 最小值 User.objects.all().aggregate(Min='age')
Count 统计数量 User.objects.all().aggregate(Count='age')
```

8. 多表查询之反向查询：当在user表和diary表之间所有的关联的时候，通过user模型借助diary关联的条件进行查找user的时候，我们称之为反向查找，例如：

`user = User.objects.filter(diary_id=2) # 就是说查找在diary表中id为2的diary这个队列中的user列`

9. 多表查询之查询关联信息：通过主对象选择需要查找的表对应的related_name,通过value查询具体信息如下

```
user = user.objects.get(pk=1)
user.diary.values('count) # 返回id为1的用户的diary的countent信息
user.diary.count() # 返回id为1用户的diary关联数量，user.diary就是Diary模型，我们可以通过它再去调用更多方法，比如get filter再去扩展查询。
```

#### 第三方ORM SQLAlchemy

SQLAlchemy是Python社区最知名的orm工具之一，为了高效和高性能的数据库访问设计，实现了完整的企业级持久模型，他可以搭配在任何一个python的web框架中，其中比较出名的是flask。常用的基础模块包括declarative_base 初始化sql与模块化的基础模块，`Base=declarative_base()`; create_engine 数据库引擎，连接数据库 `engine = create_engine('mysql+pymysql://root:@localhost:3306/sqlalchemy_test')`; sessionmake 数据插入查询的模块 `db_session=sessionmaker(bind=engine)()`。