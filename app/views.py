from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ContactForm
from .models import Contactmodel

def home(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fi_name = request.POST.get('Firstname')
            li_name = request.POST.get('Lastname')
            num = request.POST.get('Phonenumber')
            name = fi_name[:2] + li_name[:2] + num[:2]


            obj = Contactmodel()
            obj.name = name
            obj.Firstname = form.cleaned_data['Firstname']
            obj.Lastname = form.cleaned_data['Lastname']
            obj.email = form.cleaned_data['email']
            obj.Phonenumber = form.cleaned_data['Phonenumber']
            obj.password = form.cleaned_data['password']
            obj.save()
       
            context = { 
                'username': name
                # 'email': obj.email
            }
            return render(request, 'success.html', context)
            
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

def success(request):
    return render(request,'success.html')