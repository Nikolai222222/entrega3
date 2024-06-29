from django.shortcuts import render




def index(request):
    return render(request, 'index.html')



def listadoSQL(request):
    # Tu lógica para la vista listadoSQL
    return render(request, 'listadoSQL.html')

def clientesAdd(request):
    # Tu lógica para la vista clientesAdd
    return render(request, 'clientesAdd.html')

def clientes_del(request, pk):
    # Tu lógica para la vista clientes_del
    return render(request, 'clientes_del.html', {'pk': pk})

def clientes_findEdit(request, pk):
    # Tu lógica para la vista clientes_findEdit
    return render(request, 'clientes_findEdit.html', {'pk': pk})

def clientesUpdate(request):
    # Tu lógica para la vista clientesUpdate
    return render(request, 'clientesUpdate.html')

def crud_generos(request):
    # Tu lógica para la vista crud_generos
    return render(request, 'crud_generos.html')

def generosAdd(request):
    # Tu lógica para la vista generosAdd
    return render(request, 'generosAdd.html')
