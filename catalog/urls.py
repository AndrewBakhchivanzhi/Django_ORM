from django.urls import path
from catalog.views import some_title

urlpatterns = [
    path('', some_title)]