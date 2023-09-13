from employee_information.models import Employees
from rest_framework import serializers

class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'nama', 'keterangan']