from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import FinancialSummary
from .form import FinancialForm

def base(request): 
    return render(request, "base.html")

def Singup(request):
    
    if request.method == "GET":
        return render(request, "singup.html", {'form': UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username =request.POST["username"], password= request.POST["password1"])
                user.save()
                return redirect("gestion")
            except IntegrityError:
                return render(request, "singup.html", {"form": UserCreationForm(),
                                                       "error": "El usuario ya existe"})

def login_ (request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render (request, "login.html",{"form": AuthenticationForm(),
                                                  "error": "Nombre o contraseña invalidas",})
        else: 
            login (request, user)
            return redirect("gestion")

def logout (request):
    logout(request, {"error": "Algo salio mal"})
    redirect ("base")

def gestion(request):
    if request.method == "GET":
        summaries = FinancialSummary.objects.filter(user=request.user)
        total_gastos = 0
        total_ingresos = 0
        for i in summaries:
            total_gastos += i.gastos
            total_ingresos += i.ingresos
        return render(request, "gestion.html", {"summaries": summaries, "total_gastos": total_gastos,
                                                "total_ingresos": total_ingresos})
    else: 
        return redirect ("añadir")
        
def añadir_datos(request):
    if request.method == "GET":
        return render(request, "añadir_datos.html", {"form": FinancialForm()})
    else:
        try: 
            form = FinancialForm(request.POST)
            datos = form.save(commit=False)
            datos.user = request.user
            datos.save()
            return redirect ("gestion")
        except ValueError: 
            return render(request, "añadir_datos.html", {"form": form, "error": "Algo salio mal"})

def eliminar_datos(request,gasto_id):
    gasto = get_object_or_404(FinancialSummary,pk=gasto_id,user=request.user)
    if request.method == "POST":
        gasto.delete()
        return redirect('gestion')    

def editar_datos(request,gasto_id):
    dato = get_object_or_404(FinancialSummary,pk=gasto_id)
    if request.method == "GET":
        form = FinancialForm(instance=dato)
        return render(request, "editar_datos.html", {"dato": dato ,"form": form})
    else:
        form = FinancialForm(request.POST, instance=dato)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.user = request.user  
            gasto.save()
            return redirect("gestion")
        else:
            return render(request, "editar_datos.html", {"dato": dato, "form": form, "error": "Datos inválidos"})
            
        
        
            
            


        

    