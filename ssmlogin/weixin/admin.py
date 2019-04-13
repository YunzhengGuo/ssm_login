from django.contrib import admin

# Register your models here.
from .models import Student, Tlogin, homework


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pub_date')
    list_filter = ('id', 'name', 'pub_date')
    search_fields = ('id', 'name', 'pub_date')
    # list_editable = ( 'author',)
    list_editable = ('id', 'name', )
    list_display_links = None
    list_per_page = 10
admin.site.register(Student, StudentAdmin)

class TloginAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date',  'stu_id')
    list_filter = ('id', 'pub_date',  'stu_id')
    search_fields = ('id', 'pub_date',  'stu_id')
    list_per_page = 10


admin.site.register(Tlogin, TloginAdmin)
class homeworkAdmin(admin.ModelAdmin):
    list_display = ('stu_id', 'name',  'homework_name','path','time')
    list_filter = ('stu_id', 'name',  'homework_name','path','time')
    search_fields =('stu_id', 'name',  'homework_name','path','time')
    list_per_page = 10


admin.site.register(homework, homeworkAdmin)