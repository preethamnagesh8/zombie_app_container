from django.urls import path
from .views import zombie_attack_list

urlpatterns = [
    path('attacks/', zombie_attack_list, name='zombie_attack_list'),
]
