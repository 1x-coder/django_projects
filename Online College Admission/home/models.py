from django.db import models
from datetime import datetime

# Create your models here.
#imagefile=image
#Image=Contact
#

#dummy
#class Post(models.Model):
#  title = models.TextField()
#    cover = models.ImageField(upload_to='images/')

#   def __str__(self):
#        return self.title

#dummy1
# class Contact(models.Model):
    # name = models.CharField(max_length=122, default="")
    # image=models.ImageField(upload_to="images/", null=True, verbose_name="", default="")
#    
# 
    # def __str__(self):
        # return self.name
#dummy1

class Contact(models.Model):
    name = models.CharField(max_length=122, default="")
    father = models.CharField(max_length=122, default="")
    mother = models.CharField(max_length=122, default="")
    email = models.CharField(max_length=122, default="")
    phone = models.CharField(max_length=12, default="")
    phone1 = models.CharField(max_length=12, default="")
    MhtcetAppNo = models.CharField(max_length=12, default="")
    MhtcetPercentile = models.CharField(max_length=12, default="")
    MhtcetRank = models.CharField(max_length=12, default="")
    JeeAppNo = models.CharField(max_length=12, default="")
    JeePercentile = models.CharField(max_length=12, default="")
    JeeRank = models.CharField(max_length=12, default="") 
    Address1 = models.TextField( default="")
    Address2 = models.TextField( default="")
    CollegeName = models.CharField(max_length=122, default="")
    Percentage = models.CharField(max_length=12, default="")
    file = models.FileField( default="")
    file1 = models.FileField( default="")
    Aadhar = models.CharField(max_length=12, default="")
    desc = models.TextField( default="")
    # date = models.DateField(default=datetime.today())
    #image=models.ImageField(upload_to="images/", null=True, verbose_name="", default="")


    def __str__(self):
        return self.name

class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()