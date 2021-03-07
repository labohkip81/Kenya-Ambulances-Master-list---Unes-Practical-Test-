from django.urls import path, include

from .views import Homepage

app_name = "institutions"


urlpatterns = [
    path('', Homepage.as_view(), name='home'),
]
