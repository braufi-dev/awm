from django.shortcuts import render
from .models import Location
# Create your views here.


def map_view(request):
    locations = Location.objects.all()
    return render(request, 'map.html', {'locations': locations})