"""ssmlogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
app_name ='weixin'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('signin/', views.signin),
    path('', views.add_Student),
    path('get_task/', views.get_task),
    path('homeworked/', views.homeworked),
    path('count_signin/', views.count_signin),
    path('add_student/', views.add_Student),
    path('login/', views.login,name='login'),
]
