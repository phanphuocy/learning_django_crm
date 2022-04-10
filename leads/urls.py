from django.urls import path
from .views import index, show

app_name = 'leads'

urlpatterns = [
    path('', index),
    path('<pk>', show)
]