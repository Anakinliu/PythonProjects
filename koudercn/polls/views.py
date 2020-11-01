from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# from django.template import loader

# Create your views here.
from polls.models import Question


def index(request):
    # 这个减号 意思是按照时间倒序，即显示最新的 5 条。
    # 从数据库获取数据
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    # 把下面的合并成一句的写法
    return render(request, 'toupiao/index.html', context)
    # # 加载静态页面
    # template = loader.get_template('toupiao/index.html')
    # # 传递参数，返回HttpResponse对象
    # return HttpResponse(template.render(context, request))


def results(request, q_id):
    return HttpResponse(f'你在查看问题：{q_id} 的结果。')


def vote(request, q_id):
    return HttpResponse(f'你在给问题：{q_id} 投票')


def detail(request, q_id):
    # try:
    #     question = Question.objects.get(pk=q_id)
    # except Question.DoesNotExist:
    #     raise Http404("不存在此问答")
    # 合成一步
    # get_object_or_404将一个Django模型作为第一个位置参数，后面可以跟上任意数量的关键字参数，如果对象不存在则弹出Http404错误。
    question = get_object_or_404(Question, pk=q_id)
    return render(request, 'toupiao/detail.html', {'question': question})
