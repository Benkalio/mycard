
from django.urls import path

from . import views

urlpatterns = [
    # ADDING DYNAMIC PATH
    path("<int:month>", views.mycard_in_numbers),
    path("<str:month>", views.mycard, name="card-month"),
]
