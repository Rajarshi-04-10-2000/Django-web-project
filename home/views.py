from django.shortcuts import render, HttpResponse, redirect
#import Contacts from models
from home.models import Contact
#import datetime
from datetime import datetime
#added msg dependecy from google(django msg framework) to show profile updated
from django.contrib import messages
#authorization
from django.contrib.auth.models import User


#s1 import HttpResponse
# Create your views here.
#change 1 is index function


def index(request):
    context = {
             'variable': "this is sent value"
    }
    #return HttpResponse("this is home page")#string render krne ke liye http response ko use krna padtha hai
    # this is how we render templets and context is a dictionery used to push value to html
    return render(request, 'index.html', context)
#change 2 creating an about page


def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

#change 3 services page


def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")
#change 4 contacts page


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('pass')
        if len(name) < 2 or len(email) < 3 or len(phone) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, password=password, date=datetime.today())
            contact.save()
            messages.success(request, 'Profile updated')

    return render(request, 'contacts.html')
    #return HttpResponse("this is contacts page")

    #output


def output(request):
    name = Contact.objects.all()
    phone = Contact.objects.all()[0].phone

    #if(phone == "9789091524"):
    #phone = "lorem ipsum "
    phone = int(phone)
    phone = phone*0;
    #name = name.values_list()
    #k = name[0]
    context = {
             'Name': name,
             'Phone': phone
             }
    return render(request, 'output.html', context)
