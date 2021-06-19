from typing import Container
import django
from django.http import HttpRequest, response
from django.http import HttpResponse
from django.shortcuts import render, redirect
from admin_contactos.models import Contactos 
from admin_contactos.forms import formContactos



def inicio(request):
    contactos = Contactos.objects.all()
    data={
        "contactos": contactos
    }
    return render(request, "index.html", data)



def registrarContacto(request):
    
    if request.method == 'POST':

        form = formContactos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'registrar.html', {'form': form, 'img_obj': img_obj})
    else:
        form = formContactos()
    return render(request, 'registrar.html', {'form': form})



def actualizarContacto(request, id_con):
    contactos = Contactos.objects.get(id = id_con)

    if request.method == 'POST':
        form = formContactos(request.POST, request.FILES, instance=contactos)
        if form.is_valid():
            form.save()
            return redirect(to="Inicio")
    else:
        form = formContactos(instance=contactos)
       
    context = {'form': form}
    return render(request, "actualizar.html", context)




def eliminarContacto(request, id_con):
    contacto = Contactos.objects.get(id = id_con)
    contacto.delete()
    return redirect(to="Inicio")