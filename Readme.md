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
