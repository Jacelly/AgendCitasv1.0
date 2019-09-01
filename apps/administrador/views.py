import json
from rest_framework.views import APIView

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.administrador.forms import RegistroForm

from apps.administrador.serializers import UserSerializer
#from django.core.mail import send_mail 
#from django.conf import settings

# Create your views here.
def index(request):
	#return HttpResponse("Soy la pagina principal de la app administrador")
	return render(request,'tratamiento/index.html')


class RegistroAdministrador(CreateView):
	model = User
	template_name = "administrador/registrarAdministrador.html"
	#form_class = UserCreationForm
	form_class = RegistroForm
	success_url = reverse_lazy('tratamiento_listar')
class UserAPI(APIView):
	serializer = UserSerializer
	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)
		return HttpResponse(json.dumps(response.data), content_type='application/json')
 
	