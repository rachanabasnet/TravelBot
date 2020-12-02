from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null = True)

#     def __str__(self):
#         return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    image = models.ImageField(upload_to='img')
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

# class Order(models.Model):
#     customer = models.ForeignKey(Customer, max_length=200,null=True, blank=True, on_delete=models.SET_NULL)
#     #Hotel = models.ForeignKey(Hotel, max_length=200,null=True, blank=True, on_delete=models.SET_NULL)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=False)
#     transaction_id = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.transaction_id


class BookHotel(models.Model):
    customer = models.ForeignKey(User, max_length=200,null=True, blank=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, max_length=200,null=True, blank=True, on_delete=models.SET_NULL)
    no_of_rooms = models.IntegerField(default=0, null=True, blank=True)
    no_of_days = models.IntegerField(default=0, null=True, blank=True)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}_{self.hotel.name}'

    @property
    def get_total(self):
        total = self.hotel.price * self.no_of_days * self.no_of_rooms
        return total

# class Payment(models.Model):
#     customer = models.ForeignKey(Customer, max_length=200,null=True, blank=True, on_delete=models.SET_NULL)
#     hotel_booked = models.ForeignKey(BookHotel, max_length=200,null=True, blank=True, on_delete=models.SET_NULL)
#     address = models.CharField(max_length=100, null=True)
#     city = models.CharField(max_length=100, null=True)
#     state = models.CharField(max_length=100, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.address