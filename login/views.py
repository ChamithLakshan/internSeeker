from django.shortcuts import render
from .models import Intern

# Create your views here.
def login(request):
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
        intern.password = request.POST['password1']
        pw2 = request.POST['password2']
        intern.save()

        return render(request, 'login.html')

        
    else:
        return render(request, 'signup.html')