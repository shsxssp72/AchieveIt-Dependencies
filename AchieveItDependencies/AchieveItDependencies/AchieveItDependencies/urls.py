from django.urls import path
from . import views

urlpatterns = [
    path('personnel/all', views.personnel_list_all),
    path('personnel/byId', views.personnel_by_id),
    path('personnel/byName', views.personnel_by_name),
    path('customer/all', views.customers_list_all),
    path('customer/byId', views.customers_by_id),
    path('customer/byCoordinator', views.customers_by_coordinator),
    path('customer/byName', views.customers_by_name),
]
