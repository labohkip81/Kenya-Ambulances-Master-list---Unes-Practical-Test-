from django.urls import path

from .views import Homepage, AmbulanceCreateView, AmbulanceUpdateView

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('add-ambulance/', AmbulanceCreateView.as_view(), name='create-ambulance'),
    path('update-ambulance/<int:pk>/', AmbulanceUpdateView.as_view(), name='update-ambulance'),

]
