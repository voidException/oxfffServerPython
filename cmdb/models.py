
from django.db import models
import json
# Create your models here.
from django.db.models.functions import datetime


class UserInfor (models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)

    def _unicode__(self):
        return '%s' % (self.catname)
    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
# Create your models here.
class ScienceNews(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    first_module = models.CharField(max_length=30, default="News")
    second_module = models.CharField(max_length=30, default="Latest News")
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=60, null=True)
    publish_date = models.CharField(max_length=35, null=True)
    content = models.TextField(null=True)
    crawl_date = models.CharField(max_length=35, null=True)
    from_url = models.CharField(max_length=350, null=True)

######### 葡萄互助数据库表 ############

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




























