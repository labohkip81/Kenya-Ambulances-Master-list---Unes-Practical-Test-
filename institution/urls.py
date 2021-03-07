from django.urls import path

from .views import Homepage, AmbulanceCreateView, AmbulanceUpdateView, AmbulanceDeleteView

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('add-ambulance/', AmbulanceCreateView.as_view(), name='create-ambulance'),
    path('update-ambulance/<int:pk>/', AmbulanceUpdateView.as_view(), name='update-ambulance'),
    path('delete-ambulance/<int:pk>/', AmbulanceDeleteView.as_view(), name='delete_ambulance'),
]
