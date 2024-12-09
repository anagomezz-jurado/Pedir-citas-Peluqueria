from django.shortcuts import render, get_object_or_404, HttpResponse

from .forms import CitaForm
from .models import Cliente, Cita, Dependienta


def index(request):
    c = Cliente.objects.all()
    return render(request, "index.html", {"clientes": c})

def lista(request):
    citas = Cita.objects.all()
    return render(request, 'lista.html', {'citas': citas})


def anadir_cita(request):
    try:
        request.session['cliente'] = request.GET['login']
    except:
        pass
    c = Cliente.objects.get(id=1)
    if request.method == "POST":
        form = CitaForm(request.POST)
        print("recibido formulario cita")
        if form.is_valid():
            nuevaCita = Cita(fecha=form.cleaned_data["fecha"], hora=form.cleaned_data["hora"], servicio=form.cleaned_data["servicio"], dependienta=form.cleaned_data["dependienta"])
            print(form.cleaned_data["nombre"].id)
            nuevaCita.save()
            cliente =Cliente.objects.get(id=form.cleaned_data["nombre"].id)
            print(cliente)
            nuevaCita.nombre.add(cliente)
            nuevaCita.save()
            print("añadida cita")
            return lista(request)
    formulario = CitaForm()
    return render(request, "anadir_cita.html", {"formulario": formulario, "cliente": c})

def borrar_cita(request):
    cita = request.GET['seleccionado']
    print(cita)
    Cita.objects.get(id=cita).delete()
    return lista(request)


def mostrar_dependienta(request):
    dependientas = Dependienta.objects.all()

    return render(request, 'mostrar_dependienta.html', {'dependientas': dependientas})

def lista_clientes(request):
    c = Cliente.objects.all()
    return render(request, "lista_clientes.html", {"clientes": c})

def tu_vista(request):
    if request.method == 'POST':
        # Lógica para el manejo de la solicitud POST
        return HttpResponse('Datos enviados correctamente.')
    else:
        # Lógica para el manejo de otras solicitudes (GET, por ejemplo)
        return render(request, 'index.html')