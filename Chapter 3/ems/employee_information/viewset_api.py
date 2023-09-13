from employee_information.models import Employees
from employee_information.serializers import EmployeesSerializers
from rest_framework import viewsets

class EmployeesViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers