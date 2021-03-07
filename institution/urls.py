from django.urls import path

from .views import (
                Homepage, 
                AmbulanceCreateView, 
                AmbulanceUpdateView, 
                AmbulanceDeleteView,
                InstitutionCreateView,
                InstitutionUpdateView,
                InstitutionDeleteView,
                InstitutionDetailView,
                search_view
            )

urlpatterns = [
    path('', Homepage, name='home'),
    path('add-ambulance/', AmbulanceCreateView.as_view(), name='create-ambulance'),
    path('update-ambulance/<uuid:pk>/', AmbulanceUpdateView.as_view(), name='update-ambulance'),
    path('delete-ambulance/<uuid:pk>/', AmbulanceDeleteView.as_view(), name='delete_ambulance'),
    path('create-institution/', InstitutionCreateView.as_view(), name='create-institution'),
    path('update-institution/<uuid:pk>/', InstitutionUpdateView.as_view(), name='update-institution'),
    path('delete-institution/<uuid:pk>/', InstitutionDeleteView.as_view(), name='delete-institution'),
    path('institution/<uuid:pk>/', InstitutionDetailView.as_view(), name='institution_detail'),
    path('search-institution/', search_view,name='search-institution'),
]
