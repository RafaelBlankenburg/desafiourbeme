from django.urls import path
from .views import home
from .views import result

urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result'),
]