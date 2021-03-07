from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from .models import Ambulance, Institution
from .forms import AmbulanceForm

# Create your views here.
class Homepage(ListView):
    template_name = 'pages/home.html'
    context_object_name = 'ambulance_list'


    def get_queryset(self):
        return Institution.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

    
    

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
