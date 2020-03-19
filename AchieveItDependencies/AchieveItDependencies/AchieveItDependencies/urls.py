from django.urls import path
from . import views

urlpatterns = [
    path('dependency/personnel/all', views.personnel_list_all),
    path('dependency/personnel/byId', views.personnel_by_id),
    path('dependency/personnel/byName', views.personnel_by_name),
    path('dependency/customer/all', views.customers_list_all),
    path('dependency/customer/byId', views.customers_by_id),
    path('dependency/customer/byCoordinator', views.customers_by_coordinator),
    path('dependency/customer/byName', views.customers_by_name),
    path('dependency/projectId/all', views.project_id_list_all),
    path('dependency/businessField/all', views.business_field_list_all),
]
