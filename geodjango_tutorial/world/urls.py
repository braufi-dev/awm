from django.urls import path
from . import views


urlpatterns = [
    path('map/', views.map_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('update_location/', views.update_location, name='update_location'),
]