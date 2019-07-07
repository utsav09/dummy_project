from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_data, name='view_3'),
    path('delete/<int:id>', views.delete, name='delete_3'),
    path('update/<int:id>', views.update_data, name='update_3'),
    path('updated/<int:id>', views.updated, name='updated_3'),
    path('save/', views.save_data, name='save_3'),
]
