from django.db import models
import datetime
import pytz
from django.contrib.auth.models import User
from django.forms import ModelForm
# from .models import User

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True ,blank=True)

    def __str__(self):
        return 'Message From' + self.name + ' ---->' + self.email


class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
        ]
    bookid = models.AutoField(primary_key=True)
    # bookid = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='Education')
    bookprice= models.DecimalField(decimal_places=0, max_digits=10000, null=True)
    bookdesc=models.TextField(max_length=500)
    timeStamp = models.DateTimeField(auto_now_add=True ,blank=True)
    require_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    # require_date = models.DateTimeField(auto_now=True)
    Tenatative_Return_Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return str(self.name)


# class Change(models.Model):
#     # bookupdateid=models.primary_key('Bookupdateid')
#     bookeditid = models.AutoField(primary_key=True)
#     bookupdate=models.ForeignKey('bookid')
#     name=models.CharField(max_length=30)
#     author=models.CharField(max_length=40)
#     bookprice= models.DecimalField(decimal_places=0, max_digits=10000, null=True)
#     bookdesc=models.TextField(max_length=500)
#     change = Change.objects.get(id='change_id')
#     # change.endtime=datetime.now()
#     change.save()
#     def __str__(self):
#         return str(self.name)
    

# class Edit(models.Model):
#     catchoice= [
#         ('education', 'Education'),
#         ('entertainment', 'Entertainment'),
#         ('comics', 'Comics'),
#         ('biography', 'Biographie'),
#         ('history', 'History'),
#         ]
#     ebookid = models.AutoField(primary_key=True)
#     bookid = models.AutoField(foreign_key=True)
#     ename=models.CharField(max_length=30)
#     eauthor=models.CharField(max_length=40)
#     ecategory=models.CharField(max_length=30,choices=catchoice,default='Education')
#     ebookprice= models.DecimalField(decimal_places=2, max_digits=10000)
#     ebookdesc=models.TextField(max_length=500)
#     etimeStamp = models.DateTimeField(auto_now_add=True ,blank=True)
#     erequire_date = models.DateTimeField(blank=True, null=True)
#     eTenatative_Return_Date = models.DateTimeField(blank=True, null=True)
#     def __str__(self):
#         return str(self.name)
