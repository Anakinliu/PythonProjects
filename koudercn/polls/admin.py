from django.contrib import admin
from .models import Question,Choice
# Register your models here.
# 管理页面无法看到投票应用，必须先在admin中进行注册，
# 告诉admin站点，请将polls的模型加入站点内，
# 接受站点的管理。
admin.site.register(Question)
admin.site.register(Choice)
