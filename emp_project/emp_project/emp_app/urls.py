from django.urls import path
from .views import add_employee,get_employee_details,get_emp_by_id,dlt_by_id
urlpatterns=[
    path("add_emp/",add_employee),
    path("get_data",get_employee_details),
    path("get_by_id/<int:emp_id>/",get_emp_by_id),
    path("dlt_id/<int:emp_id>/",dlt_by_id)
]