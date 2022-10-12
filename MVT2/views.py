
import random
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from Person.models import Person

def Home(request):
    template = loader.get_template("Home.html")
    render_template = template.render({})
    return HttpResponse(render_template)

def create_person(request,nombre,apellido,nrofav):
    Persona = Person.objects.create(nombre=nombre, apellido=apellido, nrofav=nrofav, fecha_consulta=datetime.now())
    Persona.save()
    template = loader.get_template('create_person.html')
    render_template = template.render({})
    return HttpResponse(render_template)

def view_person(request):
    Persona = Person.objects.all()
    template = loader.get_template('view_person.html')
    render_template = template.render({'Persona': Persona})
    return HttpResponse(render_template)