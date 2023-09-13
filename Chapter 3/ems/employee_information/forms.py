from django import forms
from employee_information.models import Pegawai


class EmployeeForm(forms.Form):
    code = forms.CharField(max_length=20)
    name = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)
    department = forms.CharField(max_length=50)
    position = forms.CharField(max_length=50)


class PegawaiForm(forms.ModelForm):
    class Meta:
        model = Pegawai
        fields = "__all__"
