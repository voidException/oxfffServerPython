from django.db import models
import json
# Create your models here.

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


#####################





























