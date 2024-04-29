from django.db import models # type: ignore
from django.utils import timezone # type: ignore

# Create your models here.

#The following clas is for the information of the courses
class Post(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=10)
    instruction_mode = models.CharField(max_length=12)
    part_of_term = models.CharField(max_length=15)
    credits = models.IntegerField()
    campus = models.CharField(max_length=20)
    days = models.DateTimeField()
    location =  models.CharField(max_length=10)