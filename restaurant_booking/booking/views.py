from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required

#Create reservation
def book_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
        
        else:
            
            form = ReservationForm()
        return render(request, 'booking/book_reservation.html', {'form': form})


#View Reservation
@login_required
def view_reservation(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'booking/view_reservations.html', {'reservations': reservations})


#Update Reservation
@login_required
def update_reservation(request, reservation_id):