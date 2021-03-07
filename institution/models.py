from django.db import models
from django.conf import settings
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField
from mapbox_location_field.models import LocationField 
from django.urls import reverse

User = settings.AUTH_USER_MODEL

INSTITUTION_TYPE = (
    ("GOV", "GOVERNMENT"),
    ("PRIV", "PRIVATE INSTITUTION"),
)

AMBULANCE_STATUS = (
    ("AVAILABLE", "AVAILABLE"),
    ("ENGAGED", "ENGAGED"),
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
    logo = models.ImageField(upload_to='media/', null=True)
    location = LocationField(
        map_attrs={
            "marker_color": "blue",
            "center": [36.8219, -1.2921],
            "zoom": 8,
        },
       
    )
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
        

    def save(self, *args, **kwargs):
        lon = self.location[0]
        lat = self.location[1]
        print(lon)
        print(lat)
        self.latitude = lat
        self.longitude = lon
        super(Institution, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("institution_detail", kwargs={"pk": self.pk})
    

    
    
    

class Ambulance(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    plate_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=AMBULANCE_TYPES)
    image = models.ImageField(upload_to='media/')
    services = models.TextField()
    status = models.CharField(choices=AMBULANCE_STATUS, max_length=50, default='AVAILABLE')
    capacity = models.IntegerField()
    request_contact = PhoneNumberField()
    created = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.plate_number
    
