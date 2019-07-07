from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_data, name='view_4'),
    path('delete/<int:id>', views.delete, name='delete_4'),
    path('update/<int:id>', views.update_data, name='update_4'),
    path('updated/<int:id>', views.updated, name='updated_4'),
    path('save/', views.save_data, name='save_4'),
]
