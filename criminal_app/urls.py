from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_record', add_record, name='add_record'),
    path('update_record/<int:pk>', update_record, name='update_record'),
    path('delete_record/<int:pk>', delete_record, name='delete_record')
]