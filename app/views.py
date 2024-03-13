from django.shortcuts import render
from app.models import Employees
from app.serializers import EmployeesSerializer
from django.http import JsonResponse


# Create your views here.



def employeesview(request):
    employee = Employees.objects.all()
    serializer = EmployeesSerializer(employee, many=True)
    return JsonResponse({"employees": serializer.data},safe=False)
