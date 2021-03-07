import folium
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import (
            CreateView, 
            UpdateView, 
            DeleteView, 
            ListView, 
            DetailView)
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.gis.geoip2 import GeoIP2


from .models import Ambulance, Institution
from .forms import AmbulanceForm, InstitutionForm


def get_geo(ip):
    """Gets geolocation using ip address specified."""
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat, lon = g.lat_lon(ip)
    return country, city, lat, lon

def get_center_coordinates(latA, longA, latB=None, longB=None):
    cord = (latA, longA)

    if latB:
        cord = [(latA + latB) / 2, (longA + longB) / 2]

    return cord


# Create your views here.
def Homepage(request): #noqa
    """
    List institutions in a map view using Folium & leaflet.js
    """
    
    institutions = Institution.objects.all()
    ip = "154.123.172.215"
    country, city, lat, lon = get_geo(ip)
    location_lat = lat
    location_lon = lon
    m = folium.Map(
        location=get_center_coordinates(location_lat, location_lon), zoom_start=8
    )
    # Location marker for institutions.
    for x in institutions:
        html = f'<a href="{x.get_absolute_url()}" target="a_blank"> <span>{x.name}</span> <img src="{x.logo.url}"> </a>'
        title = f"{x.name}"
        popup = folium.Popup(html)
        folium.Marker(
            [x.latitude, x.longitude],
            tooltip=title,
            popup=popup,
            icon=folium.Icon(color="purple"),
        ).add_to(m)
   
    m = m._repr_html_()
    
    context = {
        "map": m,
    }
    print(context)

    return render(request, 'pages/home.html', context)





    
    

class AmbulanceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create a new ambulance instance
    """
    model = Ambulance
    template_name = 'pages/create_ambulance.html'
    success_url = reverse_lazy('home')
    success_message = 'Ambulance has been created successfully'
    form_class = AmbulanceForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.uploaded_by = self.request.user
        return super(AmbulanceCreateView, self).form_valid(form)



class AmbulanceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Ambulance
    template_name = 'pages/create_ambulance.html'
    success_url = reverse_lazy('home')
    success_message = 'Ambulance has been details have been updated successfully'
    form_class = AmbulanceForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.uploaded_by = self.request.user
        return super(AmbulanceUpdateView, self).form_valid(form)

    

class AmbulanceDeleteView(LoginRequiredMixin, SuccessMessageMixin,DeleteView):
    model = Ambulance
    success_url = reverse_lazy('home')
    success_message = 'Ambulance instance has been deleted successfully'


class InstitutionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create a new institution instance
    """
    model = Institution
    template_name = 'institution/institution_create.html'
    success_url = reverse_lazy('home')
    success_message = 'Instituion has been created successfully'
    form_class = InstitutionForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.uploaded_by = self.request.user
        return super(InstitutionCreateView, self).form_valid(form)

class InstitutionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update and existing institution instance
    """
    model = Institution
    template_name = 'institution/institution_create.html'
    success_url = reverse_lazy('home')
    success_message = 'Instituion has been created successfully'
    form_class = InstitutionForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.uploaded_by = self.request.user
        return super(InstitutionUpdateView, self).form_valid(form)

class InstitutionDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete an institution instance
    """
    model =  Institution
    success_url = reverse_lazy('home')


class InstitutionDetailView(DetailView):
    """
    Institutions Detail View
    """
    model = Institution
    template_name = 'institution/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ambulances"] = Ambulance.objects.all()
        return context
    