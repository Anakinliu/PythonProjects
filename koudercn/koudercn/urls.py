"""
接下来，在项目的主urls.py文件中添加urlpattern条目，
指向我们刚才建立的polls这个app独有的urls.py文件，
这里需要导入include模块。

include语法相当于多级路由，
它把接收到的url地址去除与此项匹配的部分，
将剩下的字符串传递给下一级路由urlconf进行判断。
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('gly/', admin.site.urls),
]
