from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from . models import Members
from . forms import NewUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
     return render(request, 'members/home.html', {})
@login_required(login_url='/accounts/login/')
def index(request):
    members = Members.objects.all()
    return render(request,'members/index.html',{'members': members} )
@login_required(login_url='/accounts/login/')
def add(request):
    return render(request, 'members/add.html')
@login_required(login_url='/accounts/login/')
def addrecord(request):
      name = request.POST['name']
      email = request.POST['email']
      member = Members(name=name, email=email)
      member.save()
      return HttpResponseRedirect(reverse('members:index'))
@login_required(login_url='/accounts/login/')
def delete(request, id):
     member = Members.objects.get(id=id)
     member.delete()
     return HttpResponseRedirect(reverse('members:index'))
@login_required(login_url='/accounts/login/')
def update(request, id):
     member = Members.objects.get(id=id)
     return render(request, 'members/update.html',{'member':member})
@login_required(login_url='/accounts/login/')
def updaterecord(request, id):
     name = request.POST['name']
     email = request.POST['email']
     member = Members.objects.get(id=id)
     member.name = name
     member.email = email
     member.save()
    # print('hET')
     return HttpResponseRedirect(reverse('members:index'))
def register(request):
     if request.method == 'POST':
          form = NewUser(request.POST)
          if form.is_valid():
               form.save()
               return redirect('login')
     else:
          form = NewUser()
     return render(request, 'registration/register.html', {'form': form})
def login(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']

          user = authenticate(username = username, password = password)
          if user is not None:
               login(request, user)
               return HttpResponseRedirect(reverse('members:index'))
          else:
               return HttpResponseRedirect(reverse('members:register'))
     return render(request, 'members/login.html', {})
def logout_view(request):
     logout(request)
     return redirect('members:home')