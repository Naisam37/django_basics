from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.

def index(request) :
    
    person = {
        'name' :'naisam',
        'age'  : '20',
        'place': 'calicut',
        'qualification': 'BCA',
        
    }
    
    numbers = {
         'num1' : 10,
         'num2' : 20,
         'num3' : 30,
         'num4' : 40,
         'num5' : 50,
         'num6' : 60,
    }
    numb = {
        'nums' : [1,2,3,4,5,6,7,8,9,10,],
        'fruits': ['apple', 'banana', 'orange']
    }
    
    context = {  # RENDER ONE ARGUEMENT ONLY RECIEVE CHEYYOLU SO CONTEXT AKI PASS CHEYTHA ELLAM PASS AKAM 
        **person,
        **numbers,# ** IS USED FOR UNPACKING AND MERGING 2 DICTIONARIES
        **numb,
    }
    

    return render(request,'index.html',context)
 
def about (request) :
    return render(request, 'about.html')

def bookings (request) :
    
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'confirmation.html')
            
    
    form = BookingForm()
    dict_form = {
        'form' : form
    }
    
    return render(request, 'bookings.html',dict_form)

def doctors (request):
    
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    
    return render(request, 'doctors.html',dict_docs)

def contact (request) :
    return render(request,'contact.html')

def departments (request) :
    
     dict_dept = {
         
        'dept' :Departments.objects.all()
            
       }
    
     return render(request, 'departments.html',dict_dept)

def template_inheritance (request) :
    return render(request, 'template_inheritance.html')


    

