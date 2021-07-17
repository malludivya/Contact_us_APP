from django.shortcuts import render

# Create your views here.
from .models import Contact
def home(request):
    return render(request,'index.html')


def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        
        data=Contact(name=name,email=email,message=message)
        data.save()


    return render(request,'contact.html')