
from django.urls import path

from newapp.views import newapp

urlpatterns = {
    path('', newapp.as_view(), name='newapp'),
}