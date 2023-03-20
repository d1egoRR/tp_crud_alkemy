from django.contrib import admin

from personas.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ("id", "nombre", "apellido", "dni")


admin.site.register(Cliente, ClienteAdmin)
