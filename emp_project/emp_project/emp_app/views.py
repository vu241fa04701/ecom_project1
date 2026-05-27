import json
from MySQLdb.constants.FIELD_TYPE import JSON
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from emp_app.models import Employee
from http import HTTPStatus
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError



@csrf_exempt
def add_employee(request):

    try:

        if request.method == 'POST':

            data = json.loads(request.body)

            emp_data = Employee.objects.create(
                name=data.get("name"),
                emp_id=data.get("emp_id"),
                email=data.get("email"),
                phone=data.get("phone"),
                gender=data.get("gender"),
                designation=data.get("designation"),
                address=data.get("address"),
                emp_type=data.get("emp_type"),
                salary=data.get("salary"),
            )

            return JsonResponse({
                "message": "Employee added successfully",
                "emp_id": emp_data.emp_id,
                "status": HTTPStatus.OK
            })

        return JsonResponse({
            "message": "Only POST method allowed",
            "status": HTTPStatus.BAD_REQUEST
        })

    except IntegrityError as e:

        return JsonResponse({
            "message": "Database Integrity Error",
            "error": str(e),
            "status": HTTPStatus.BAD_REQUEST
        })

    except Exception as e:

        return JsonResponse({
            "message": "Something went wrong",
            "error": str(e),
            "status": HTTPStatus.INTERNAL_SERVER_ERROR
        })
def get_employee_details(request):
    """
    this function is returning all the details of the employee table
    :param request:
    :return:
    """
    try:

        emp_data = Employee.objects.all().values()
        response_data = list(emp_data)

        return JsonResponse({
            "data": response_data,
            "status": HTTPStatus.OK
        })

    except Exception as e:

        return JsonResponse({
            "message": "Unable to fetch employee data",
            "error": str(e),
            "status": HTTPStatus.INTERNAL_SERVER_ERROR
        })
def get_emp_by_id(request,emp_id):
    """
    this function takes id as a input through url and return the data of that user
    :param request:
    :param emp_id:
    :return:
    """
    try:

        emp_by_id = Employee.objects.get(emp_id=emp_id)

        return JsonResponse({
            "name": emp_by_id.name,
            "emp_id": emp_by_id.emp_id,
            "email": emp_by_id.email,
            "phone": emp_by_id.phone,
            "gender": emp_by_id.gender,
            "designation": emp_by_id.designation,
            "address": emp_by_id.address,
            "emp_type": emp_by_id.emp_type,
            "salary": emp_by_id.salary,
            "status": HTTPStatus.OK
        })

    except ObjectDoesNotExist:

        return JsonResponse({
            "message": "Employee not found",
            "status": HTTPStatus.NOT_FOUND
        })

    except Exception as e:

        return JsonResponse({
            "message": "Something went wrong",
            "error": str(e),
            "status": HTTPStatus.INTERNAL_SERVER_ERROR
        })
"""
or 
emp_by_id=Employee.objects.get(emp_id=emp_id
return JsonResponse({
"name":emp_by_id.name,
"emp_id":emp_by_id.emp_id,
"email":emp_by_id.email,
"phone":emp_by_id.phone,
"gender":emp_by_id.gender,
"designation":emp_by_id.designation,
"address":emp_by_id.address,
"emp_type":emp_by_id.emp_type,
"salary":emp_by_id.salary 
})
"""
def dlt_by_id(request,emp_id):
    try:

        employee = Employee.objects.get(emp_id=emp_id)
        employee.delete()

        emp_data2 = Employee.objects.all().values()
        response_data = list(emp_data2)

        return JsonResponse({
            "message": "Employee deleted successfully",
            "emp_id": emp_id,
            "data": response_data,
            "status": HTTPStatus.OK
        })

    except ObjectDoesNotExist:

        return JsonResponse({
            "message": "Employee not found",
            "status": HTTPStatus.NOT_FOUND
        })

    except Exception as e:

        return JsonResponse({
            "message": "Unable to delete employee",
            "error": str(e),
            "status": HTTPStatus.INTERNAL_SERVER_ERROR
        })

