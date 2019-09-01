from django.urls import path,include,re_path
from apps.administrador import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	 path('', login_required(views.index), name='index'),
	 path('registrar/', login_required(views.RegistroAdministrador.as_view()), name="registrar_Admin"),
	  path('api/', login_required(views.UserAPI.as_view()), name='api'),
]
