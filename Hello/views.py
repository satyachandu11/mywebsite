from django.shortcuts import render, HttpResponse
from Hello.models import Contact, Quotes
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    #return HttpResponse("This is About Us Page!")

def home(request):
     return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def postq(request):
    return render(request, "postq.html")    

def result(request):
    result_list = Quotes.objects.all
    return render(request, "result.html",
    {'result_list' : result_list}) 

def postq(request):
    if request.method =="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        age=request.POST.get('age')
        location=request.POST.get('location')
        quot=request.POST.get('quot')
        postq=Quotes(firstname=firstname, lastname=lastname, age=age, location=location, quot=quot,date=datetime.today()) 
        postq.save()
        messages.success(request, 'Your Quote has been posted Successfully!')
    return render(request, "postq.html")       

def contact(request):
    if request.method =="POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         desc=request.POST.get('desc')
         contact=Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today()) 
         contact.save() 
         messages.success(request, 'Your message has been sent!')
        
    return render(request, "contact.html")
    
    #return HttpResponse("This is Contact Us Page!")     