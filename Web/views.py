from django.shortcuts import render, HttpResponse, redirect
from Web.models import Formulario
from django.contrib import messages

# Create your views here.

def home(request):
    
    return render(request, 'paginas/home.html')

def nosotros(request):
    
    return render(request, 'paginas/nosotros.html')

def productos(request):

    return render(request, 'paginas/productos.html')

def faq(request):

    return render(request, 'paginas/faq.html')

def publicaciones(request):

    return render(request,'paginas/publicaciones.html')

def contacto(request):

     return render(request, 'paginas/contacto.html')

def save_formulario(request):
    
    if request.method == 'POST':

        nombre = request.POST['Nombre']
        apellido = request.POST['Apellido']
        dni = request.POST['DNI']
        nacionalidad = request.POST['Nacionalidad']
        edad = request.POST['Edad']
        telefono = request.POST['Telefono']
        email = request.POST['Email']
        empresa = request.POST['Empresa']
        consulta = request.POST['Consulta']
        comentarios = request.POST['Comentarios']
            
        formulario = Formulario(
            nombre = nombre,
            apellido = apellido,
            dni = dni,
            nacionalidad = nacionalidad,
            edad = edad,
            telefono = telefono,
            email = email,
            empresa = empresa,
            consulta = consulta,
            comentarios = comentarios
        )

        formulario.save()

        messages.success(request, 'Formulario Enviado!!!<')
        return redirect('contacto')

        
    else:
        return HttpResponse("<h2>No se ha enviado el formulario</h2>")
    
    
def login(request):

    return render(request, 'paginas/login.html')
