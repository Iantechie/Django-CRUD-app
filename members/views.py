from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from . models import Members
from . forms import NewUser

# Create your views here.
def index(request):
    members = Members.objects.all()
    return render(request,'members/index.html',{'members': members} )

def add(request):
    return render(request, 'members/add.html')

def addrecord(request):
      name = request.POST['name']
      email = request.POST['email']
      member = Members(name=name, email=email)
      member.save()
      return HttpResponseRedirect(reverse('members:index'))
def delete(request, id):
     member = Members.objects.get(id=id)
     member.delete()
     return HttpResponseRedirect(reverse('members:index'))
def update(request, id):
     member = Members.objects.get(id=id)
     return render(request, 'members/update.html',{'member':member})
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
     return render(request, 'members/register.html')
