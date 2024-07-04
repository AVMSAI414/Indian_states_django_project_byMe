from django.urls import path,include
from India.views import *

app_name="India"

urlpatterns = [
    path('States/',States,name='States'),
]
