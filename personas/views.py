from django.shortcuts import render

from personas.models import Cliente


def listado_cliente(request):
    clientes = Cliente.objects.all()

    return render(
        request,
        "personas/listado.html",
        {'clientes': clientes}
    )


def crear_cliente(request):

    if request.POST:
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        dni = request.POST['txtDni']

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            dni=dni,
        )

    return render(request, "personas/crear.html")
