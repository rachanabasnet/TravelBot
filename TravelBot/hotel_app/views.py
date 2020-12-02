from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.contrib import messages
from .models import *

# Create your views here.
def hotel(request):
    hotels = Hotel.objects.all()
    context={
        'title':'Hotels',
        'hotels':hotels
    }
    return render(request, 'hotel_app/hotels.html', context)

@login_required
def booking(request, id):
    if request.method == "POST":
        customer = request.user
        hotel = Hotel.objects.get(id=id)
        no_of_rooms = request.POST.get('no_of_rooms')
        no_of_days = request.POST.get('no_of_days')  
        Booking = BookHotel(customer=customer, hotel= hotel, no_of_rooms= no_of_rooms, no_of_days=no_of_days)
        Booking.save()
        messages.success(request, f'Booking Complete!!! Now Checkout for Payment!!!')

        return redirect('checkout')
    else:
        form = BookingForm 
        a = {'form':form} 
        return render(request, 'hotel_app/bookhotel_form.html', a)


def checkout(request):
    item = BookHotel.objects.latest('id')
    context={'title':'BookHotel', 'item': item}
    return render(request, 'hotel_app/checkout.html', context)

def booking_details(request, id):
    items = BookHotel.objects.all().filter(customer_id=id)
    context={'title':'BookHotel', 'items': items}
    return render(request, 'hotel_app/booking_details.html', context)
