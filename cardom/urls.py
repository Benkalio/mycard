
from django.urls import path

from . import views

urlpatterns = [
    # ADDING DYNAMIC PATH
    path("<month>", views.mycard)
]
