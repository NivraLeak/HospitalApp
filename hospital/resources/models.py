import uuid

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Resource(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField()
    available =models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=False, unique=True)
    image = models.ImageField(upload_to='resources/',null=False,blank=False)

    #def save(self,*args,**kwargs):
    #    self.slug = slugify(self.type)
    #    super(Resource,self).save(*args,**kwargs)

    def __str__(self):
        return self.type

def set_slug(sender,instance,*args,**kwargs):
    if instance.type and not instance.slug:
        slug = slugify(instance.type)

        while Resource.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.type, str(uuid.uuid4())[:8] )
            )


        instance.slug = slug


pre_save.connect(set_slug, sender = Resource)
