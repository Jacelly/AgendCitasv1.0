from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core import serializers
from apps.tratamiento.forms import TratamientoForm
from apps.tratamiento.models import Tratamiento
# Create your views here.
def listado(request):
	lista = serializers.serialize('json', Tratamiento.objects.all().order_by('tratam_id'))
	return HttpResponse(lista, content_type='application/json')
def index(request):
	#return HttpResponse("Index Hola mundo!!")
	return render(request,'tratamiento/index.html')
def tratamiento_view(request):
	if request.method == 'POST':
		form = TratamientoForm(request.POST) 
		if form.is_valid():
			form.save()
		#return HttpResponseRedirect(reverse(index))
		return redirect('tratamiento_listar')
	else:
		form = TratamientoForm()
	return render(request, 'tratamiento/tratamiento_form.html', {'form':form})
def tratamiento_list(request):
	tratamiento = Tratamiento.objects.all().order_by('tratam_id')
	contexto = {'tratamientos':tratamiento}
	return render(request, 'tratamiento/tratamiento_list.html', contexto)
def tratamiento_edit(request,id_tratamiento):
	tratamiento = Tratamiento.objects.get(tratam_id=id_tratamiento)
	if request.method == 'GET':
		form = TratamientoForm(instance=tratamiento)
	else:
		form =TratamientoForm(request.POST,instance=tratamiento)
		if form.is_valid():
			form.save()
		return redirect('tratamiento_listar')
		#return HttpResponseRedirect(reverse(tratamiento_list))
	return render(request,'tratamiento/tratamiento_form.html', {'form':form})
def tratamiento_eliminar(request, id_tratamiento):
	tratamiento = Tratamiento.objects.get(tratam_id=id_tratamiento)
	if request.method == 'POST':
		tratamiento.delete()
		return redirect('tratamiento_listar')
		#return HttpResponseRedirect(reverse(tratamiento_list))
	return render(request, 'tratamiento/tratamiento_delete.html', {'tratamiento':tratamiento})


class TratamientoList(ListView):
	model = Tratamiento
	template_name = 'tratamiento/tratamiento_list.html'
	paginate_by=3
class TratamientoCreate(CreateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'tratamiento/tratamiento_form.html'
    success_url = reverse_lazy('tratamiento_listar')
class TratamientoUpdate(UpdateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'tratamiento/tratamiento_form.html'
    success_url = reverse_lazy('tratamiento_listar')
class TratamientoDelete(DeleteView):
	model = Tratamiento
	template_name = 'tratamiento/tratamiento_delete.html'
	success_url = reverse_lazy('tratamiento_listar')