from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
    path('search',views.ResourceSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ResourceDetailView.as_view(),name='resource'),
]
