from .models import ResourceAllocation

def get_or_create_resourceAllocation(request):
    user = request.user if request.user.is_authenticated else None
    resourceAllocation_id = request.session.get('resourceAllocation_id')
    resourceAllocation = ResourceAllocation.objects.filter(resourceAllocation_id=resourceAllocation_id).first()

    if resourceAllocation is None:
        resourceAllocation= ResourceAllocation.objects.create(user=user)

    if user and resourceAllocation.user is None:
        resourceAllocation.user = user
        resourceAllocation.save()
    request.session['resourceAllocation_id'] = resourceAllocation.resourceAllocation_id

    return resourceAllocation
