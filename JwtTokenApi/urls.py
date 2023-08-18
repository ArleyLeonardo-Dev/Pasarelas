from django.urls import path
from .views import *

urlpatterns = [
    path('JWT/', JwtApiView.as_view() , name = 'token_obtain_pair'),
]