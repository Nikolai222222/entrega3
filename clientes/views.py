# clientes/views.py

from django.shortcuts import render, get_object_or_404
from .models import Genero, Cliente  # Importa los modelos de la aplicación
from .forms import GeneroForm  # Importa el formulario si es necesario

def index(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "clientes/index.html", context)

def listadoSQL(request):
    clientes = Cliente.objects.raw("SELECT * FROM clientes_cliente")
    context = {"clientes": clientes}
    return render(request, "clientes/listadoSQL.html", context)

def clientesAdd(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        nombre = request.POST.get("nombre")
        aPaterno = request.POST.get("paterno")
        aMaterno = request.POST.get("materno")
        fechaNac = request.POST.get("fechaNac")
        genero = request.POST.get("genero")
        telefono = request.POST.get("telefono")
        email = request.POST.get("email")
        direccion = request.POST.get("direccion")
        
        objGenero = get_object_or_404(Genero, id_genero=genero)
        Cliente.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=True  # Usando True en lugar de 1 para activo
        )
        context = {"mensaje": "Datos guardados satisfactoriamente"}
        return render(request, "clientes/clientes_add.html", context)
    else:
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, "clientes/clientes_add.html", context)

def clientes_del(request, pk):
    cliente = get_object_or_404(Cliente, rut=pk)
    cliente.delete()
    mensaje = "Eliminado satisfactoriamente"
    clientes = Cliente.objects.all()
    context = {'clientes': clientes, 'mensaje': mensaje}
    return render(request, "clientes/clientes_list.html", context)

def clientes_findEdit(request, pk):
    cliente = get_object_or_404(Cliente, rut=pk)
    generos = Genero.objects.all()
    context = {'cliente': cliente, 'generos': generos}
    return render(request, "clientes/clientes_edit.html", context)

def clientesUpdate(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        cliente = get_object_or_404(Cliente, rut=rut)
        cliente.nombre = request.POST.get("nombre")
        cliente.apellido_paterno = request.POST.get("paterno")
        cliente.apellido_materno = request.POST.get("materno")
        cliente.fecha_nacimiento = request.POST.get("fechaNac")
        genero = request.POST.get("genero")
        cliente.id_genero = get_object_or_404(Genero, id_genero=genero)
        cliente.telefono = request.POST.get("telefono")
        cliente.email = request.POST.get("email")
        cliente.direccion = request.POST.get("direccion")
        cliente.activo = True  # Usando True en lugar de 1 para activo
        cliente.save()

        generos = Genero.objects.all()
        context = {"mensaje": "Datos actualizados satisfactoriamente", "generos": generos, "cliente": cliente}
        return render(request, "clientes/clientes_edit.html", context)
    else:
        clientes = Cliente.objects.all()
        context = {"clientes": clientes}
        return render(request, "clientes/clientes_list.html", context)

def crud_generos(request):
    generos = Genero.objects.all()
    context = {"generos": generos}
    return render(request, "clientes/generos_list.html", context)

def generosAdd(request):
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            form = GeneroForm()
            context = {"mensaje": "Datos guardados satisfactoriamente", "form": form}
            return render(request, "clientes/generos_add.html", context)
    else:
        form = GeneroForm()
    context = {'form': form}
    return render(request, "clientes/generos_add.html", context)

