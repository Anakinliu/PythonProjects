from django.db import models
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    # 每一个字段都是Field类的一个实例
    question_text = models.CharField(max_length=200)
    # 每一个Field实例的名字就是字段的名字
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # 在你的Python代码中会使用这个值，你的数据库也会将这个值作为表的列名。
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
