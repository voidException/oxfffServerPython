# -*- coding: utf-8 -*-
import simplejson
import sys
from MySQLdb.compat import unicode
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import  HttpResponse
# Create your views here.
from  cmdb import  models
from django.core import serializers
from django.core.serializers import serialize,deserialize
from django.db.models.query import QuerySet
import django.utils
from django.conf import settings
from cmdb.models import Fruit


# user_list=[
#     {"user":"jack","pwd":"abc"},
#     {"user":"tom","pwd":"123456"},
# ]

class Employee:
    '所有员工的基类'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
# -*- encoding: UTF-8 -*-
class Student:
  name = ''
  age = 0
  def __init__(self, name, age):
    self.name = name
    self.age = age
def convert_to_dict(obj):
  '''把Object对象转换成Dict对象'''
  dict = {}
  dict.update(obj.__dict__)
  return dict
def convert_to_dicts(objs):
  '''把对象列表转换为字典列表'''
  obj_arr = []
  for o in objs:
    #把Object对象转换成Dict对象
    dict = {}
    dict.update(o.__dict__)
    obj_arr.append(dict)
  return obj_arr
def class_to_dict(obj):
  '''把对象(支持单个对象、list、set)转换成字典'''
  is_list = obj.__class__ == [].__class__
  is_set = obj.__class__ == set().__class__
  if is_list or is_set:
    obj_arr = []
    for o in obj:
      #把Object对象转换成Dict对象
      dict = {}
      dict.update(o.__dict__)
      obj_arr.append(dict)
    return obj_arr
  else:
    dict = {}
    dict.update(obj.__dict__)
    return dict

stu = Student('zhangsan', 20)

############这儿是返回json数据#################
def ajax_get_data(request):
    # data = convert_to_dict(stu)  #这个是可以用的，适用于普通对象返回json，用Student类做了示范
    # print(data)
    # return HttpResponse(json.dumps(data), content_type="application/json")

    # row=models.UserInfo.objects.get(id=2)   #这个是ok的，适用于将数据库表的一条记录转为json返回
    # print(row.toJSON())
    # data=row.toJSON()
    # return HttpResponse(data, content_type="application/json")

    #print(models.UserInfor.objects.all())
    json_data = serializers.serialize("json", models.UserInfor.objects.all())
    print(json_data)
    #print(json_data[9])

    return HttpResponse(json_data, content_type="application/json")
## 资讯列表接口
def newslist(request):
    newsData={"key":"aaaa"};
    if request.method == "POST":
        newsData=serializers.serialize("json",models.news.objects.all())
    return  HttpResponse(newsData,content_type='application/json')


##############葡萄互助，登录#############################
def index(request):
    #return HttpResponse("hello  world!")
    #return  render(request,"index.html",)
    #####这儿是获得post传过来的数据
    Fruit.objects.filter(name="chichi").update(name="chihechihe", price="100")
    print(request.method)
    return  render(request,"index.html",{"data":{}})


def loginaction(request):
    user_list = [
            {"user":"jack","pwd":"abc"},
            {"user":"tom","pwd":"123456"},
         ]
    helpadmin = {}
    if request.method=="POST":
        username=request.POST.get("username",None)
        #print(username)
        password=request.POST.get("password",None)
        if(username=="" or password==""):
            print("aaa")
            return render(request,"main.html",{"data":user_list}) #重定向到错误页面
        #使用用户名和密码获取数据库的数据
        try:
            helpadmin=models.helpadmin.objects.get(adminname=username)
            print(helpadmin.adminname)
            user_list.append( {"user":helpadmin.adminname,"pwd":"123456"})
            return render(request, "error.html", {"data":{"user":helpadmin.adminname,"pwd":"123456"}})
            #return render(request, "error.html", helpadmin)
        except BaseException:
            print("出错了")

        if helpadmin is None:
            print("bbb")
            user_list = {"recode": "2001", "msg": "用户名或者密码错误"}

            return render(request, "main.html", {"data": user_list})
    else:
        print("GET method")
        return render(request, "main.html", {"data": user_list})












