from django.urls import path

from . import views
app_name = 'resourcesAllocation'

urlpatterns = [
    path('',views.resourceAllocation,name = 'resourceAllocation'),
    path('agregar',views.add, name = 'add'),
    path('eliminar',views.remove, name = 'remove')
]
