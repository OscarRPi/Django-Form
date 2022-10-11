from django.urls import path  
from formapp import views  

urlpatterns = [   
    path('', views.read, name="read"),  
    path('create',views.create, name="create"),
    path('update/<int:id>', views.update, name="update"), 
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),  
]  
