
from django.urls import path,include
from apps.tratamiento import views
from django.contrib.auth.decorators import login_required
urlpatterns = [

   path('', login_required(views.index), name='index'),
   #path('nuevo/', views.tratamiento_view, name="tratamiento_crear"),
   path('nuevo/', login_required(views.TratamientoCreate.as_view()), name="tratamiento_crear"),
   #path('listar/', views.tratamiento_list, name="tratamiento_listar"),
   path('listar', login_required(views.TratamientoList.as_view()), name="tratamiento_listar"),
   path('editar/<pk>',login_required(views.TratamientoUpdate.as_view()), name='tratamiento_editar'),
   #path('editar/<int:id_tratamiento>', views.tratamiento_edit, name='tratamiento_editar'),
    path('eliminar/<pk>', login_required(views.TratamientoDelete.as_view()), name='tratamiento_eliminar'),
   #path('eliminar/<int:id_tratamiento>', views.tratamiento_eliminar, name='tratamiento_eliminar'),
  #path('listado/', login_required(listado), name='listado'),
  	path('listado/', views.listado, name='listado'),
]
