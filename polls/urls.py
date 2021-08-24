from django.urls import path
from . import views

# A path has 4 variables 
# route, view, optional; kwargs,name
 
urlpatterns = [
    path('', views.index, name='index'),
]