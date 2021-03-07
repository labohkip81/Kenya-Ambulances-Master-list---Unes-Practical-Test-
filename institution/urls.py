from django.urls import path

from .views import (
                Homepage, 
                AmbulanceCreateView, 
                AmbulanceUpdateView, 
                AmbulanceDeleteView,
                InstitutionCreateView,
                InstitutionUpdateView,
                InstitutionDeleteView
            )

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('add-ambulance/', AmbulanceCreateView.as_view(), name='create-ambulance'),
    path('update-ambulance/<int:pk>/', AmbulanceUpdateView.as_view(), name='update-ambulance'),
    path('delete-ambulance/<int:pk>/', AmbulanceDeleteView.as_view(), name='delete_ambulance'),
    path('create-institution/', InstitutionCreateView.as_view(), name='create-institution'),
    path('update-institution/<int:pk>/', InstitutionUpdateView.as_view(), name='update-institution'),
    path('delete-institution/<int:pk>/', InstitutionDeleteView.as_view(), name='delete-institution'),
]
