"""
为了调用该视图，我们还需要编写urlconf，
也就是路由配置。
在polls目录中新建一个文件，名字为urls.py（不要换成别的名字）
"""
from django.urls import path

from . import views

# 在整个project里属于二级路由
urlpatterns = [
    path('', views.index, name='index'),
]