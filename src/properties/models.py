from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.

# class Status_Property(models.Model):
#     category = models.CharField(max_length=100)

#     def __str__(self):
#         return self.category

class Property_Information(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    address = models.TextField(max_length=10000)
    BHK = models.IntegerField()
    image = models.ImageField()
    area = models.CharField(max_length=500,default='0sqft')
    price = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pincode = models.IntegerField()
    parking = models.BooleanField(default=0)
    small_thumbnail = models.ImageField()
    STATUS_CHOICE = (
        ('Rent','Rent'),
        ('Sale','Sale'),
        ('Under-Construction','Under-Construction'),
    )
    status = models.CharField(max_length=100,choices=STATUS_CHOICE,default='Rent')
    FURNISHING_CHOICE = (
        ('Un-Furnished','Un-Furnished'),
        ('Semi-Furnished','Semi-Furnished'),
        ('Furnished','Furnished'),
        ('Fully-Furnished','Fully-Furnished'),
    )
    furnishing = models.CharField(max_length=100,choices=FURNISHING_CHOICE)
    AMENITIES_CHOICE = (
        ('Gym','Gym'),
        ('Swimming Pool','Swimming Pool'),
        ('Garden','Garden'),
        ('Club House','Club House'),
        ('Cafe Area','Cafe Area'),
        ('Children Play Area','Children Play Area'),
        ('Intercom','Intercom'),
    )
    amenities = MultiSelectField(choices=AMENITIES_CHOICE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('property_detail',kwargs={
            'id':self.id
        })
