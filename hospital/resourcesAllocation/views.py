from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from.models import ResourceAllocationResources
from resources.models import Resource

from .models import ResourceAllocation
from .utils import get_or_create_resourceAllocation

def resourceAllocation(request):
    #request.session['resourceAllocation_id'] = None
    resourceAllocation = get_or_create_resourceAllocation(request)

    return render(request,'resourcesAllocation/resourceAllocation.html',{
        'resourceAllocation':resourceAllocation
    })

def add(request):
    resourceAllocation = get_or_create_resourceAllocation(request)
    resources = get_object_or_404(Resource,pk=request.POST.get('resource_id'))
    quantity = request.POST.get('quantity',1)

    #resourceAllocation.resources.add(resource, through_defaults={
    #    'quantity': quantity
    #})

    resourceallocation_resources = ResourceAllocationResources.objects.create(resourceAllocation=resourceAllocation,
                                                resources=resources,quantity=quantity)
    return render(request, 'resourcesAllocation/add.html',{
        'resource':resources
    })

def remove(request):
    resourceAllocation = get_or_create_resourceAllocation(request)
    resource = get_object_or_404(Resource, pk=request.POST.get('resource_id'))

    resourceAllocation.resources.remove(resource)

    return redirect('resourcesAllocation:resourceAllocation')
