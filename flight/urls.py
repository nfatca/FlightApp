from django.urls import path, include
from .views import FlightView, ReservationView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'flights', FlightView)
router.register(r'reservations', ReservationView)

urlpatterns = [


]
urlpatterns += router.urls
