
from django.db import models
import json
from django.db.models.functions import datetime

######### 葡萄筹 ############
# Userc 葡萄筹的用户
class Userc(models.Model):
    id=models.BigAutoField(primary_key=True)
    userName=models.CharField(max_length=60)
    userPass=models.CharField(max_length=60)
    registerDate=models.DateTimeField('注册日期',default=datetime.timezone.now)


# 资讯表
class news(models.Model):
    id=models.BigAutoField(primary_key=True)
    newsuuid=models.CharField(max_length=60)
    author=models.CharField(max_length=30,null=True)
    publishdate=models.DateTimeField('保存日期', default = datetime.timezone.now)
    title=models.CharField(max_length=60,null=True)
    vicetitle=models.CharField(max_length=60,null=True)
    source=models.CharField(max_length=60,null=True)
    newscontent=models.CharField(max_length=5000,null=True)
    imageone=models.CharField(max_length=600,null=True)
    imagetwo=models.CharField(max_length=600,null=True)
    imagethree=models.CharField(max_length=600,null=True)
    newsurl=models.CharField(max_length=600,null=True)
    newstype=models.CharField(max_length=10,null=True)
    lable=models.CharField(max_length=60,null=True)
    def __str__(self):  # __unicode__ on Python 2
        return self.newsuuid

# 管理员表
class helpadmin(models.Model):
    adminid=models.BigAutoField(primary_key=True)
    adminuuid=models.CharField(max_length=60)
    adminname=models.CharField(max_length=60)
    adminpasswd=models.CharField(max_length=60)
    def __str__(self):
        return self.adminid + self.adminuuid + self.adminname + self.adminpasswd

# 学习Django建立的表
class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    price=models.CharField(max_length=20)



























