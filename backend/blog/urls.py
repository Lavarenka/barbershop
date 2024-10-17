# myapp/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', form_view, name='form_view'),

    # path('', contact, name='contact'),
]