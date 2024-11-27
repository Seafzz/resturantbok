from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required

# Create reservation
def book_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()  
    return render(request, 'booking/book_reservation.html', {'form': form})

# View Reservation
@login_required
def view_reservation(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'booking/view_reservations.html', {'reservations': reservations})

# Update Reservation
@login_required
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)  # Ensure it's the user's reservation
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view_reservations')
    else:
        form = ReservationForm(instance=reservation)  # Pre-populate the form 
    return render(request, 'booking/update_reservation.html', {'form': form, 'reservation': reservation})

# Cancel Reservation
@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    reservation.delete()
    return redirect('view_reservations')

# Home page view
def home(request):
    return render(request, 'home.html')

# Reservation success page
def reservation_success(request):
    return render(request, 'booking/reservation_success.html')