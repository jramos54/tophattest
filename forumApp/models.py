from django.db import models

# Create your models here.

class forum(models.Model):
  name=models.CharField(max_length=200, default="anonimo")
  email=models.CharField(max_length=200)
  topic=models.CharField(max_length=300,null=True)
  description=models.CharField(max_length=2000,blank=True)
  date_created=models.DateTimeField(auto_now_add=True,null=True)

  def __str__(self):
    return str(self.topic)


class discussion(models.Model):
  forum=models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
  name=models.CharField(max_length=200,default="anonimo")
  discuss=models.CharField(max_length=3000)

  def __str__(self):
    return str(self.forum)
