from django.db import models

# Create your models here.
class mtlbobj(models.Model):
    obj=models.FileField( upload_to="media")
    mtl=models.FileField( upload_to="media")