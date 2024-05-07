from django.db import models

# Create your models here.

#Event class
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
 
    class Meta:  
        db_table = "tblevents"