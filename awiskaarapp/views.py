from django.shortcuts import render, redirect
from django.http import HttpResponse
from awiskaarapp.models import Contact

# Create your views here.
def home(request):
    return render(request, 'awiskaarapp/index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name = name, email = email, subject = subject, message = message)
        contact.save()
    
    return render(request, 'awiskaarapp/index.html')