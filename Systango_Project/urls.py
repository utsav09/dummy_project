from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', admin.site.urls, name='datas'),
    path('', views.home, name='home'),
    path('register/', include('registration.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('database_1/', include('database_1.urls')),
    path('database_2/', include('database_2.urls')),
    path('database_3/', include('database_3.urls')),
    path('database_4/', include('database_4.urls')),
    path('database_5/', include('database_5.urls')),
    path('database/', include('databases.urls')),

]

urlpatterns += staticfiles_urlpatterns()
admin.site.site_header = "Systango Project"
admin.site.site_title = "Systango Project"
admin.site.index_title = "Database Control Panel"
