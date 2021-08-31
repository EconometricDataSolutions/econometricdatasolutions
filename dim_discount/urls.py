
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from dim_discount import views 
from employee_register import views as employee_register_views

from .dash_apps.finished_apps import dim_discount_datatable 

#app_name = 'employee_register'

urlpatterns = [
    url('employee/', employee_register_views.employee_list, name='employee_register'),
    path('dim_discount_upload/', views.simple_upload),
    #path('employee/', employee_register_views.employee_list, name='employee_register'),
    #path('employee/', include('employee_register.urls')),

]
 