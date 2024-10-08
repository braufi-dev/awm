from django.urls import path
from . import views

app_name = 'map'  # Declare the app name for namespacing

urlpatterns = [
    path('map/', views.map_view, name='map'),
]
