from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

INSTITUTION_TYPE = (
    ("GOV", "GOVERNMENT"),
    ("PRIV", "PRIVATE INSTITUTION"),
)

HOSPITAL_STATUS = (
    ("NOT OPERATIONAL", "NOT OPERATIONAL"),
    ("OPERATION", "OPERATIONAL"),
)

# Create your models here.
class Institution(models.Model):
    """ 
    Model to represent institution that owns a specific ambulance
    """
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=150, choices=INSTITUTION_TYPE)
    status =  models.CharField(max_length=50, choices=HOSPITAL_STATUS)
    
