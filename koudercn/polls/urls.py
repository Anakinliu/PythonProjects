"""
为了调用该视图，我们还需要编写urlconf，
也就是路由配置。
在polls目录中新建一个文件，名字为urls.py（不要换成别的名字）
"""
from django.urls import path

from . import views

# 使用URLconf的命名空间, 就叫app_name
app_name = 'polls'

# 在整个project里属于二级路由
"""
此path三元组可以理解为：浏览器的url，django的视图函数，模版里的url（避免模板中硬编码的URLs）要这么写：{% url 'polls:name有啥用' question.id %}
"""
urlpatterns = [
    # 浏览器输入：/polls
    path('', views.index, name='index'),
    # 浏览器输入：/polls/数值ID
    path('xiangxi/<int:q_id>/', views.detail, name='name有啥用'),

    path('<int:q_id>/vote', views.vote, name='vote'),

    path('<int:q_id>/results', views.results, name='results')
]