from django.shortcuts import render,redirect
from .models import Intern, Company
from django.contrib import messages
from django.contrib.auth.models import auth

# Create your views here.
def login(request):
    return render(request, 'login.html')
def logout(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def signup_intern(request):

    if request.method == 'POST':
        intern = Intern()
        intern.firstname = request.POST['first_name']
        intern.lastname = request.POST['last_name']
        intern.username = request.POST['username']
        intern.email = request.POST['email']
        pw1 = request.POST['password1']
        pw2 = request.POST['password2']

        if pw1 == pw2:
            if Intern.objects.filter(username=intern.username).exists():
                messages.info(request,'This username is already taken')
                return redirect('signup')
            elif Intern.objects.filter(email=intern.email).exists():
                messages.info(request,'This email is already used')
                return redirect('signup')
            else:
                intern.password = request.POST['password1']
                intern.save()
                messages.info(request,'Successfully Registered!')
                return render(request, 'login.html')
            
            
        else:
            messages.info(request,'Passwords not matching!')
            return redirect('signup')
    else:
        return render(request, 'signup.html')




def signup_company(request):

    if request.method == 'POST':
        company = Company()
        company.companyname = request.POST['company_name']
        company.ceoname = request.POST['ceo_name']
        company.username = request.POST['username']
        company.email = request.POST['email']
        pw1 = request.POST['password1']
        pw2 = request.POST['password2']
        if pw1 == pw2:
            if Company.objects.filter(username=company.username).exists():
                messages.info(request,'This username is already taken')
                return redirect('signup')
            elif Company.objects.filter(email=company.email).exists():
                messages.info(request,'This email is already used')
                return redirect('signup')
            else:
                company.password = request.POST['password1']
                company.save()
                messages.info(request,'Successfully Registered!')
                return render(request, 'login.html')
            
            
        else:
            messages.info(request,'Passwords not matching!')
            return redirect('signup')

        
    else:
        return render(request, 'signup.html')

def login_intern(request):
    if request.method == 'POST':
        intern = Intern()
        uname = request.POST['username']
        pw = request.POST['password']


        if Intern.objects.filter(username=uname).exists() and Intern.objects.filter(password=pw).exists():
            return render(request, 'internhome.html',{'username':uname})
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login')
    else:
        return redirect('login')


def login_company(request):
    if request.method == 'POST':
        company = Company()
        uname = request.POST['username']
        pw = request.POST['password']

        if Company.objects.filter(username=uname).exists() and Company.objects.filter(password=pw).exists():
            return render(request, 'homepage.html')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login')
    else:
        return redirect('login')

def internhome(request):
    return render(request, 'internhome.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')