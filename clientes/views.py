from django.shortcuts import render
from .models import Genero, Cliente
from .forms import GeneroForm

def index(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "clientes/index.html", context)

def listadoSQL(request):
    clientes = Cliente.objects.raw("select * FROM clientes_cliente")
    context = {"clientes": clientes}
    return render(request, "clientes/listadoSQL.html", context)

def clientesAdd(request):
    if request.method != "POST":
        print(request)
        generos = Genero.objects.all()
        context={"generos":generos}
        return render(request,"clientes/clientes_add.html", context)
    else:
        print("Entra por aqui")
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        obj=Cliente.objects.create(
            rut = rut,
            nombre = nombre,
            apellido_paterno = aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimineto = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo=1
        )
        obj.save()
        context = {"mensaje":"ok, datos guardados..."}
        return render(request,"clientes/clientes_add.html", context)

def clientes_del(request,pk):
    context = {}
    try:
        cliente=Cliente.objects.get(rut=pk)

        cliente.delete()
        mensaje = "Eliminado satisfactoriamente"
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
        return render(request,"clientes/clientes_list.html",context)
    except:
        mensaje = "Error, rut no existe"
        clientes = Cliente.objects.all()
        context = {'clientes':clientes, 'mensaje':mensaje}
        return render(request,"clientes/clientes_list.html", context)

def clientes_findEdit(request,pk):

    if pk != "":
        cliente=Cliente.objects.get(rut=pk)
        generos = Genero.objects.all()

        print(type(cliente.id_genero.genero))
        context = {'cliente': cliente, 'generos': generos}

        if cliente:
            return render(request,"clientes/clientes_edit.html", context)
        else:
            context = {"mensaje":"Error, rut no existe"}
            return render(request,"clientes/clientes_edit.html",context)

def clientesUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        cliente = Cliente()
        cliente.rut = rut 
        cliente.nombre = nombre
        cliente.apellido_paterno = aPaterno
        cliente.apellido_materno = aMaterno
        cliente.fecha_nacimiento = fechaNac
        cliente.id_genero = objGenero
        cliente.telefono = telefono
        cliente.email = email
        cliente.direccion = direccion
        cliente.activo = 1
        cliente.save()

        generos = Genero.objects.all()
        context = {"mensaje":"Datos actualizados satisfactoriamente","generos":generos, "cliente":cliente}

        return render(request,"clientes/clientes_edit.html", context)
    else:
        clientes = Cliente.objects.all()
        context = {"clientes":clientes}
        return render(request,"clientes/clientes_list.html", context)
    
def crud_generos(request):
    generos = Genero.objects.all()
    context = {"generos":generos}
    return render(request,"clientes/generos_list.html",context)

def generosAdd(request):
    print("estoy en controlador generosAdd")
    context = {}

    if request.method == "POST":
        print("el controlador es un post")
        form = GeneroForm(request.POST)
        print("Estoy en agregar, is_valid")
        form.save()
        form = GeneroForm()
        context = {
            "mensaje":"ok, Datos guardados exitosamente",
            "form":form
        }
        return render(request,"clientes/generos_add.html",context)
    else:
        form = GeneroForm()
        context = {'form':form}
        return render(request,"clientes/generos_add.html", context)