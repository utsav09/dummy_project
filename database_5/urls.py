from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_data, name='view_5'),
    path('delete/<int:id>', views.delete, name='delete_5'),
    path('update/<int:id>', views.update_data, name='update_5'),
    path('updated/<int:id>', views.updated, name='updated_5'),
    path('save/', views.save_data, name='save_5'),
]
