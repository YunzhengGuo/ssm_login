```python
#创建工程
django-admin.py startproject tango_with_django_project 
python manage.py startapp rango



#在项目的settings.py 中加入app
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'rango',
]

```

在新建的rango项目中views.py

```python
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner!")
```



在urls.py中进行如下设置

```python
from rango import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^admin/', admin.site.urls),
]
```

部署Django项目的话

一般使用的是()

```python
python manage.py runserver 0.0.0.0:8000
python manage.py runserver ip:8000
```



数据库相关操作

```python
python manage.py migrate # 创建数据库
python manage.py makemigrations rango #创建数据库的歉意
```

打开django shell

```python 
python manage.py shell
#如果原本安装了 ipython 那么这个会进入到ipython中
quuit()#退出
```

配置数据库管理界面

打开rango/admin.py

```python
from django.contrib import admin
from rango.models import Category, Page
admin.site.register(Category)
admin.site.register(Page)
```

重启服务器之后就会

127.0.0.1:8000/admin

在数据库中添加meta 类 声明 verbose_name_plural 属性就可以

```python
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
    	return self.name
```

grappelli

```python
pip install django-grappelli
pip install django-markdown
```

加admin