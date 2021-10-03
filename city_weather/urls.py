from django.urls import path, include
from .views import *

app_name = "city"

urlpatterns = [
                path('', base_city, name="base_city"),
                path('latest/', latest_search, name="latest_search"),
    ]
