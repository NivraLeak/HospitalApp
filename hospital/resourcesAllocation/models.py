import uuid
from django.db import models

from users.models import User
from resources.models import Resource

from django.db.models.signals import pre_save

class ResourceAllocation(models.Model):
    resourceAllocation_id = models.CharField(max_length=100, null=False, blank = False, unique=True )
    user = models.ForeignKey(User,null = True,blank= True, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)
    createdStart = models.DateTimeField(null = True)
    createdEnd = models.DateTimeField(null = True)

    #resources = models.ForeignKey(Resource, blank = True, null = True, on_delete = models.SET_NULL)
    resources = models.ManyToManyField(Resource,through='ResourceAllocationResources')

    def __str__(self):
        return self.resourceAllocation_id

    def resources_related(self):
        return self.resourceallocationresources_set.select_related('resources')

class ResourceAllocationResourcesManager(models.Manager):

        def create_or_update_quantity(self,resourceAllocation,resources,quantity=1):
            object, created = self.get_or_create(resourceAllocation=resourceAllocation,resources=resources)

            if not created:
                object.quantity += quantity
                object.save()
            return object
class ResourceAllocationResources(models.Model):
    resourceAllocation = models.ForeignKey(ResourceAllocation,on_delete=models.CASCADE)
    resources = models.ForeignKey(Resource,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True )

    objects = ResourceAllocationResourcesManager()

def set_resourceAllocation_id(sender,instance,*args,**kwargs):
    if not instance.resourceAllocation_id:
        instance.resourceAllocation_id = str(uuid.uuid4())

pre_save.connect(set_resourceAllocation_id,sender=ResourceAllocation)
