from django.urls import path
from . import views

urlpatterns = [
    path("Dubayok",views.function, name="none duba"),
    path("<str:item>/",views.animal,name="animals"),
    path("<int:n1>/<int:n2>/",views.summaration_ex,name="sumEx"),
    path("<int:s>/",views.redirectFun,name="redirect")
]