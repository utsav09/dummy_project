from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_data, name='view_2'),
    path('delete/<int:id>', views.delete, name='delete_2'),
    path('update/<int:id>', views.update_data, name='update_2'),
    path('updated/<int:id>', views.updated, name='updated_2'),
    path('save/', views.save_data, name='save_2'),
]
