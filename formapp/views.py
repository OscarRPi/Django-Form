# formapp/views.py

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect

from formapp.models import Data_User
from formapp.forms import DataForm

def create(request):  

    if request.method == "POST":  
        
        form = DataForm(request.POST)  
                    
        if form.is_valid(): 

            try:
                form.save()
                return redirect('/')

            except:

                return redirect('/')
    else:  
        
        form = DataForm()

    return render(request,'formapp/form.html',{'form':form}) 

def read(request): 

    users = Data_User.objects.all()
    return render(request,"formapp/index.html",{'users':users})  

def update(request, id):  

    user = Data_User.objects.get(id_usuario=id)  
    form = DataForm(request.POST, instance = user)  

    if request.method == "POST":  

        if form.is_valid():

            try:
                form.save()  
                return redirect("/")

            except:

                return redirect('/')
    else:

        form = DataForm()

    return render(request, 'formapp/edit.html', {'user':user,'form': form}) 

def edit(request, id): 

    try:
        user = Data_User.objects.get(id_usuario=id)
        return render(request,'formapp/edit.html', {'user':user})

    except:
        return redirect('/')

def delete(request, id): 

    try:
        user = Data_User.objects.get(id_usuario=id)  
        user.delete()  
        return redirect("/")

    except:
        return redirect('/')



