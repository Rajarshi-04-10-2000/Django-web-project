from django.shortcuts import render, HttpResponse
#s1 import HttpResponse
# Create your views here.
#change 1 is index function
def index(request):
    context={
             'variable':"this is sent value"
    }
    #return HttpResponse("this is home page")#string render krne ke liye http response ko use krna padtha hai
    return render(request,'index.html',context)# this is how we render templets and context is a dictionery used to push value to html
#change 2 creating an about page
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

#change 3 services page
def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")
#change 4 contacts page
def contacts(request):
    return render(request,'contacts.html')
    #return HttpResponse("this is contacts page")
