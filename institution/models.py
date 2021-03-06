from django.db import models
from django.conf import settings
from address.models import AddressField

User = settings.AUTH_USER_MODEL

INSTITUTION_TYPE = (
    ("GOV", "GOVERNMENT"),
    ("PRIV", "PRIVATE INSTITUTION"),
)

HOSPITAL_STATUS = (
    ("NOT OPERATIONAL", "NOT OPERATIONAL"),
    ("OPERATION", "OPERATIONAL"),
)

AMBULANCE_TYPES = (
    ("BASIC", "Basic Ambulance"),
    ("ADVANCE", "Advance Ambulance"),
    ("MORTUARY", "Mortuary Ambulance"),
    ("Neonatal","Neonatal Ambulance"),
    ("Patient-Transport", "Patient Transport Vehicle"),
    ("Air", "Air Ambulance"),
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
    location = AddressField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_add = True)

    def __str__(self):
        return self.name
    
    

class Ambulance(models.Model):
    institution = models.ForeignKey(Institution, verbose_name=_(""), on_delete=models.CASCADE)
    plate_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=AMBULANCE_TYPES)
    image = models.ImageField(upload_to='media/')
    services = models.TextField()
    capacity = models.IntegerField()
    request_contact = 
    created = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.plate_number
    
