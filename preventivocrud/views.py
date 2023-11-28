from django.shortcuts import render,redirect
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse

from . import forms,models

def home_view(request):
    metas=models.MetaModelo.objects.all()
    temas=models.Tema.objects.all()
    eventos=models.Evento.objects.all()
    return render(request,'home/index.html',{'metas':metas,'temas':temas,'eventos':eventos})

def CreateMeta(request):
    metaform=forms.MetaForm()
    metas=models.MetaModelo.objects.all()
    if request.method=='POST':
        metaform=forms.MetaForm(request.POST,request.FILES)
        if metaform.is_valid():
            metaform.save()
        return HttpResponseRedirect('Metas')
    return render(request,'home/ui-typography.html',{'metaform':metaform,'metas':metas})

def EditMeta(request,pk):
    metas2=models.MetaModelo.objects.get(id=pk)
    metas=models.MetaModelo.objects.all()
    metaform=forms.MetaForm(instance=metas2)
    if request.method=='POST':
        metaform=forms.MetaForm(request.POST,request.FILES,instance=metas2)
        if metaform.is_valid():
            metaform.save()
            return redirect('Metas')
    return render(request,'home/ui-typography.html',{'metaform':metaform,'metas':metas})

def DeleteMeta(request,pk):
    meta=models.MetaModelo.objects.get(id=pk)
    meta.delete()
    return redirect('Metas')

def CreateTema(request):
    temaform=forms.TemaForm()
    temas=models.Tema.objects.all()
    metas=models.MetaModelo.objects.all()
    if request.method=='POST':
        temaform=forms.TemaForm(request.POST,request.FILES)
        if temaform.is_valid():
            temaform.save()
        return HttpResponseRedirect('Temas')
    return render(request,'home/ui-tables.html',{'temaform':temaform,'temas':temas,'metas':metas})
 
def EditTema(request,pk):
    temas2=models.Tema.objects.get(id=pk)
    temas=models.Tema.objects.all()
    temaform=forms.TemaForm(instance=temas2)
    if request.method=='POST':
        temaform=forms.TemaForm(request.POST,request.FILES,instance=temas2)
        if temaform.is_valid():
            temaform.save()
            return redirect('Temas')
    return render(request,'home/ui-tables.html',{'temaform':temaform,'temas':temas})

def DeleteTema(request,pk):
    tema=models.Tema.objects.get(id=pk)
    tema.delete()
    return redirect('Temas')

def CreateEvento(request):
    eventoform=forms.EventoForm()
    eventos=models.Evento.objects.all()
    temas=models.Tema.objects.all()
    if request.method=='POST':
        eventoform=forms.EventoForm(request.POST,request.FILES)
        if eventoform.is_valid():
            eventoform.save()
        return HttpResponseRedirect('Eventos')
    return render(request,'home/ui-icons.html',{'eventoform':eventoform,'eventos':eventos})
 
def EditEvento(request,pk):
    eventos2=models.Evento.objects.get(id=pk)
    eventos=models.Evento.objects.all()
    eventoform=forms.EventoForm(instance=eventos2)
    if request.method=='POST':
        eventoform=forms.EventoForm(request.POST,request.FILES,instance=eventos2)
        if eventoform.is_valid():
            eventoform.save()
            return redirect('Eventos')
    return render(request,'home/ui-icons.html',{'eventoform':eventoform,'eventos':eventos})

def DeleteEvento(request,pk):
    evento=models.Evento.objects.get(id=pk)
    evento.delete()
    return redirect('Eventos')

def GenerateReport(request):
    eventos=models.Evento.objects.all()
    fechaform=forms.FechaForm()
    if request.method=='POST':
        fechaform=forms.FechaForm(request.POST,request.FILES)
        fecha_input = request.POST.get('fecha')
        if fechaform.is_valid():
            fecha_inicio = fechaform.cleaned_data['fecha_inicio']
            fecha_fin = fechaform.cleaned_data['fecha_fin']
            if fecha_inicio and fecha_fin:
                eventos = models.Evento.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
            else:
                eventos = models.Evento.objects.all()
            lista_eventos = []
            for evento in eventos:
                total_personas = evento.cant_hombres + evento.cant_mujeres
                info_evento = {
                        'conferencia': evento.conferencia,
                        'cursos': evento.cursos,
                        'tema': evento.tema,
                        'escuela': evento.escuela,
                        'fecha': evento.fecha,
                        'apoyo': evento.apoyo,
                        'cant_hombres': evento.cant_hombres,
                        'cant_mujeres': evento.cant_mujeres,
                        'dirigido':evento.dirigido,
                        'total_personas': total_personas,
                    }
                lista_eventos.append(info_evento)
            return render(request, 'home/ui-maps.html', {'contex':lista_eventos,'fechaform':fechaform})
        return HttpResponseRedirect('Reportes')
        
    return render(request,'home/ui-maps.html',{'fechaform':fechaform})

