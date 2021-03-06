# Generated by Django 2.1.7 on 2019-04-12 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='学生姓名')),
                ('homework_name', models.CharField(max_length=50, verbose_name='作业名')),
                ('path', models.CharField(max_length=50, verbose_name='上传路径')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '提交作业表',
                'verbose_name_plural': '提交作业表',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='学号')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '学生表',
                'verbose_name_plural': '学生信息表',
            },
        ),
        migrations.CreateModel(
            name='Tlogin',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='座位号')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='签到时间')),
                ('stu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weixin.Student', verbose_name='学生学号')),
            ],
            options={
                'verbose_name': '签到表',
                'verbose_name_plural': '签到信息表',
            },
        ),
        migrations.AddField(
            model_name='homework',
            name='stu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weixin.Student', verbose_name='学生学号'),
        ),
    ]
