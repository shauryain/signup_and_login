from django.shortcuts import render,redirect

#this is for authintication of user password
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        uemail=request.POST.get('email')
        upassword=request.POST.get('password')

        obj=User.objects.create_user(username=uname, email=uemail, password=upassword)
        obj.save()
        return redirect("/")
    else:
        return render(request, 'signup.html')
    




def error(request):
    return redirect(request,"error.html")

# def login(request):
#     if request.method == 'POST':
#         uname=request.POST.get('uname')
#         pswd=request.POST.get('upassword')
#         user= authenticate(request,username=uname,password=pswd)

#         if user is not None:
#             login(request,user)
#             return redirect("/")
#         else:
#             d = {"msg": "Invalid username or password"}
#             return render(request,"login.html", d)

#     else:

#         return render(request, "login.html")

from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pswd = request.POST.get('upassword')
        user = authenticate(request, username=uname, password=pswd)

        if user is not None:
            auth_login(request, user)  # Use the aliased function
            return redirect("/")
        else:
            d = {"msg": "Invalid username or password"}
            return render(request, "login.html", d)
    else:
        return render(request, "login.html")

