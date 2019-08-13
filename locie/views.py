from django.shortcuts import render,redirect
from .models import CustomerForm,Customer
import datetime
from django.views.generic.edit import FormView

# Create your views here.
def login(request):

    if request.method=="POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            submitted = False
            
            # ("Customer is" + Customer.objects.all())

    else:
        customer_form = CustomerForm()
        submitted=True

    return render(request,'locie/index.html',{'form':customer_form,'submitted':submitted})

def index(request):
    return render(request,'locie/index.html')
