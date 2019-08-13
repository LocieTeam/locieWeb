from django.db import models
from django import forms
# Create your models here.
class Customer(models.Model):
    email = models.EmailField(null=True,blank=True)
    first_name = models.CharField(max_length=30,default='',null=True,blank=True)
    last_name = models.CharField(max_length=30,default='',null=True,blank=True)
    phone_number = models.CharField(max_length=30,default='',null=True,blank=True)
    city = models.CharField(max_length=30,default='',null=True,blank=True)
    business_name = models.CharField(max_length=30,default='',null=True,blank=True)
    business_type = models.CharField(max_length=30,default='',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('email','first_name','last_name','phone_number','city','business_name','business_type',)
