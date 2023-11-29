from django.urls import path

from .views import home, donations, donate, initiate_stk_push
urlpatterns = [
    path('', home, name='home'),
    path('donations/', donations, name='donations'),
    path('donate/', donate, name='donate'),
    path('initiate_stk_push/', initiate_stk_push, name='initiate_stk_push'),

    
]