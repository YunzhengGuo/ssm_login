from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView

from .models import Student, Tlogin
from .forms import StudentForm, TloginForm


def signin(request):
    Tlogin_list = Tlogin.objects.order_by('-pub_date')
    l = len(Tlogin_list)
    context_dict = {
        'boldmessage':"crunchy,creamy,cokkie,candy,cuocake!",
        'L':[i for i in range(l)],
        "Tlogin_list":Tlogin_list,
    }

    return render(request,'weixin/signin.html',context=context_dict)
def signin_action(request):

    context_dict = {
        'boldmessage':"crunchy,creamy,cokkie,candy,cuocake!",
        'L':[0,1,2,4]
    }

    return render(request,'weixin/signin.html',context=context_dict)

def count_signin(request):

    return render(request,'weixin/count_signin.html')

def login(request):
    if request.method == 'POST':
        stu_id = request.POST['xuehao']
        name = request.POST['name']
        print(name)
        print(stu_id)
        a = Tlogin()
        print(Student.objects.get(id=stu_id).id)
        a.stu_id = Student.objects.get(id=stu_id)
        # a.pub_date = '2019-04-10 17:35:56.688223' 
        # print(Student.objects.get(id=stu_id)) 
        # print(dir(Student.objects.get(id=stu_id))) 
        # print(a.id)
        a.save()
        return HttpResponseRedirect('/signin')


    #     stu_list = Student.objects.all()
    #     return render(request,'weixin/signin.html',{'stu_list':stu_list})
    return render(request,'weixin/login.html')
    
def get_task(request):
    return render(request,'weixin/get_task.html')
class homework:
    def __init__(self,id,name,homework_name,path,time):
        self.id = id
        self.name = name
        self.homework_name = homework_name
        self.path = path
        self.time = time

def homeworked(request):
    homeworked_list = []
    a = homework(181164540,"于富江","jsp 大作业","c:/upload","2018-12-02 12:34:12")
    homeworked_list.append(a)
    a = homework(181164541,"申明可","信息安全 大作业","c:/upload","2018-04-01 12:34:12")
    homeworked_list.append(a)
    a = homework(181164542,"陈超","操作系统 算法 大作业","c:/upload","2018-06-13 12:34:12")
    homeworked_list.append(a)
    a = homework(181164544,"王威","组成原理 设计","c:/upload","2018-09-11 12:34:12")
    homeworked_list.append(a)
    a = homework(181164545,"高俊凯","单片机设计 大作业","c:/upload","2018-09-15 12:34:12")
    homeworked_list.append(a)
    a = homework(181164546,"高畅","c++ 课程设计","c:/upload","2018-09-22 12:34:12")
    homeworked_list.append(a)
    a = homework(181164546,"王可","java 小程序","c:/upload","2018-11-11 12:34:12")
    homeworked_list.append(a)
    a = homework(181164546,"陈硕","bbs 博客系统","c:/upload","2018-11-11 12:34:12")
    homeworked_list.append(a)
    
    return render(request,'weixin/homeworked.html',{'homeworked_list':homeworked_list})

def add_Student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            # 把新的学生信息存入数据库
            form.save(commit=True)
            #保存新的学生信息之后显示一个确认消息
            #
            return HttpResponseRedirect('/add_student')
        else:
            msg = form.errors
            print(msg)

    return render(request, 'weixin/add_student.html',{'form':form})













# def register(request):
#     if request.method == 'POST':
#         pk = request.POST.get('pk')
#         if pk:
#             student = get_object_or_404(Student,pk=pk)
#             student.name = request.POST['name']
#             student.id = request.POST['id']
#             student.save()
#             return render(request,'/weixin/register.html')
#         form = StudentForm(request.POST,request.FILES or None)
#         if form.is_valid():
#             student = form.save(commit=False)
            
#             student.save()
#         return render(request,'/weixin/register.html')

#     return render(request,'/weixin/register.html')