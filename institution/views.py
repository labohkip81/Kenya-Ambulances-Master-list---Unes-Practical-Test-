from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Ambulance, Institution

# Create your views here.
class Homepage(ListView):
    template_name = 'pages/home.html'
    context_object_name = 'ambulance_list'


    def get_queryset(self):
        return Institution.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

    
    

class CreateAmbulance(CreateView):
    """
    Create a new ambulance instance
    """
    pass


class AmbulanceUpdateView(UpdateView):
    pass

class AmbulanceDeleteView(DeleteView):
    pass
