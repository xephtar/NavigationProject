from django.urls import path

from . import views

urlpatterns = [
    path('get-last-points', views.get_last_points, name='get-last-points'),
    path('bulk-create-vehicles', views.bulk_create_vehicles, name='bulk-create-vehicles'),
    path('bulk-create-navigation-records', views.bulk_create_navigation_record, name='bulk-create-navigation-records')
]
