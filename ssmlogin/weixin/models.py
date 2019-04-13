import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Student(models.Model):
    id = models.CharField('学号',max_length=200,primary_key=True)
    pub_date = models.DateTimeField('注册时间',auto_now_add=True)
    name = models.CharField(max_length=50)
  
       
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=2)

    class Meta:
        verbose_name = '学生表'
        verbose_name_plural = '学生信息表'

class Tlogin(models.Model):
    id = models.IntegerField('座位号',auto_created=True,primary_key=True)
    pub_date = models.DateTimeField('签到时间',auto_now_add=True)
    stu_id = models.ForeignKey(Student, on_delete=models.CASCADE,verbose_name='学生学号')
    # name = models.ForeignKey(Student, on_delete=models.CASCADE,verbose_name='学生姓名')
       
   
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=2)

    class Meta:
        verbose_name = '签到表'
        verbose_name_plural = '签到信息表'


class homework(models.Model):

    id = models.ForeignKey(Student, on_delete=models.CASCADE,verbose_name='学生学号')
    name= models.CharField("学生姓名",max_length=50)
    homework_name = models.CharField("作业名",max_length=50)
    path = models.CharField("上传路径",max_length=50)
    time = models.DateTimeField('上传时间',auto_now_add=True)
    class Meta:
        verbose_name = '提交作业表'
        verbose_name_plural = '提交作业表'
