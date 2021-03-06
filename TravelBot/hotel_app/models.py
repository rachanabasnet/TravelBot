from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='img')
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class BookHotel(models.Model):
    customer = models.ForeignKey(User, max_length=200,null=True, blank=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, max_length=10000,null=True, blank=True, on_delete=models.SET_NULL)
    no_of_rooms = models.IntegerField(default=0, null=True, blank=True)
    checkin_date = models.DateTimeField(blank=True, null=True)
    checkout_date = models.DateTimeField(blank=True, null=True)
    no_of_days = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return f'{self.id}_{self.hotel.name}'

    @property
    def get_no_of_days(self):
        no_of_days = self.checkout_date - self.checkin_date
        return no_of_days

    @property
    def get_total(self):
        total = self.hotel.price * self.no_of_rooms * self.no_of_days
        return total
