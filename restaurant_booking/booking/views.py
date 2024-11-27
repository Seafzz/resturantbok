from django.shortcuts import render, redirect
from .forms import ReservationForm

def book_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
        
        else:
            
            form = ReservationForm()
        return render(request, 'booking/book_reservation.html', {'form': form})
