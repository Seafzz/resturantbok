from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_reservation, name='book_reservation'),
    path('view/', views.view_reservation, name='view_reservations'),  # Changed here
    path('update/<int:reservation_id>/', views.update_reservation, name='update_reservation'),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
]