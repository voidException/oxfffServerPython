from django.db import models
from pygments.lexers import get_all_lexers         # 一个实现代码高亮的模块
from pygments.styles import get_all_styles
# Create your models here.


class UserInfo (models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)


    def _unicode__(self):
        return '%s' % (self.catname)
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
# Create your models here.
class Sciencenews(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    first_module = models.CharField(max_length=30, default="News")
    second_module = models.CharField(max_length=30, default="Latest News")
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=60, null=True)
    publish_date = models.CharField(max_length=35, null=True)
    content = models.TextField(null=True)
    crawl_date = models.CharField(max_length=35, null=True)
    from_url = models.CharField(max_length=350, null=True)

class djangoMysqlTest(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    djangoUUI = models.CharField(max_length=30)
    book = models.CharField(max_length=30, default="")

#####################
class IDC(models.Model):
    '''机房'''
    name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.name

class Host(models.Model):
    hostname = models.CharField(max_length=64,unique=True)
    ip_addr = models.GenericIPAddressField()
    port = models.SmallIntegerField(default=22)
    idc = models.ForeignKey('IDC',blank=True,null=True)
    system_type_choices = ((0,'Linux'),(1,'Windows'))
    system_type = models.SmallIntegerField(choices=system_type_choices,default=0)
    memo = models.CharField(max_length=128,blank=True,null=True)
    enabled = models.BooleanField(default=1,verbose_name="启用本机")

    class Meta:
        unique_together = ('ip_addr','port')
        verbose_name = "主机表"
    def __str__(self):
        return "%s(%s)"%( self.hostname,self.ip_addr)




class userTest(models.Model):
    class Meta:
        db_table='user'
    id==models.AutoField(max_length=11,db_column='id',primary_key=True)
    username=models.CharField(max_length=30,db_column='username',blank=False)
    userPass=models.CharField( max_length=30,db_column='userPass',blank=False)


























