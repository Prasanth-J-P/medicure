from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from .models import Medicinedetails
from .forms import DetailsForm
from storeroomapi.serializers import ProductSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form}) 

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='/login/')
def home_page(request):
    context = {
        'user': request.user
        }
    return render(request,'homepage.html',context)


@login_required(login_url='/login/')
def Add_Medicine(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addmed')
    else:
        form = DetailsForm()
    return render(request, 'create.html', {'form': form})


@login_required(login_url='/login/')
def List_Medicine(request):
    details_list = Medicinedetails.objects.all()
    paginator = Paginator(details_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'retrieve.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def Edit_Medicine(request, pk):
    lists = Medicinedetails.objects.get(pk=pk)
    if request.method == 'POST':
        form = DetailsForm(request.POST,instance=lists)
        if form.is_valid():
            form.save()
            return redirect('listmed')
    else:
        form = DetailsForm(instance= lists)           
    return render(request, 'update.html', {'form': form})


@login_required(login_url='/login/')
def Delete_Medicine(request,pk):
    lists=Medicinedetails.objects.get(pk=pk)  
    if request.method == 'POST':
        lists.delete()
        return redirect('listmed')
    
    return render(request,'delete.html',{'lists':lists})



@login_required(login_url='/login/')
def Logout_View(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)


@login_required(login_url='/login/')
def list_medicine(request):
    meds=request.GET['search']
    if meds=='':
        return render(request,'notfound.html')   
    details_list = Medicinedetails.objects.filter(name__icontains = meds)
    if not details_list:
        return render(request,'notfound.html')
    
    return render(request, 'search.html', {'details_list': details_list})
