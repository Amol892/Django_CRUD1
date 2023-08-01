from django.urls import path 
from .views import Person_view,Home_view,Update_view,Delete_view

urlpatterns = [
    path('person/',Person_view,name='person_url'),
    path('home/',Home_view,name='home_url'),
    path('update/<int:pk>/',Update_view,name='update_url'),
    path('delete/<int:pk>/',Delete_view,name='delete_url')
    
]