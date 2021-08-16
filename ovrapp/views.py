from django.shortcuts import render , redirect
from .models import *
from .forms import OrderForm , RegsitrationForm

# Create your views here.

def create(request): 
     form = OrderForm()
     if request.method == 'POST':
         form = OrderForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('create')
     context = {'form':form}
     return render(request , 'home.html', context )

def home(request):
    if request.method == 'POST':
        form = RegsitrationForm(request.POST)
        if form.is_valid():
            #form.save()
            messages.success(request, 'New success!')
            return redirect('/home')
        else:
            messages.error(request, 'Invalid Please try again.')
    else:
        form = RegsitrationForm()
    return render(request, 'home.html', {'form': form})
  
def form2(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            #form.save()
            messages.success(request, 'New success!')
            return redirect('/form2')
        else:
            messages.error(request, 'Invalid Please try again.')
    else:
        form = OrderForm()
    return render(request, 'form2.html', {'form': form})