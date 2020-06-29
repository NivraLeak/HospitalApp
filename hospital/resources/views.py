from django.shortcuts import render

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView


from .models import Resource

class ResourceListView(ListView):
    template_name = 'index.html'
    queryset = Resource.objects.all().order_by('-id')

    def get_context_data(self,**kawargs):
        context = super().get_context_data(**kawargs)
        context['message'] = 'Listado de recursos'
        return context

class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'resources/resource.html'

    def get_context_data(self,**kawargs):
        context = super().get_context_data(**kawargs)
        context['message'] = 'Listado de recursos'

        print(context)
        return context

class ResourceSearchListView(ListView):
    template_name = 'resources/search.html'

    def get_queryset(self):
        return Resource.objects.filter(type__icontains=self.query())

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self,**kawargs):
        context = super().get_context_data(**kawargs)
        context['query'] = self.query()
        context['count'] = context['resource_list'].count()
        return context
