from django.urls import path

from .views import Homepage, AmbulanceCreateView

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('add-ambulance/', AmbulanceCreateView.as_view(), name='create-ambulance'),
]
