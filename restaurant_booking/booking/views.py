from django.shortcuts import render, redirect
from .forms import ReservationForm

def book_reservation(request):
    if request.method == 'POST':
        from = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
        else:
            form = ReservationForm()
