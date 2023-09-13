from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView
from employee_information.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Employees', EmployeesViewset)

urlpatterns = [
     path('api/', views.include(router.urls)),
    path('redirect-admin', RedirectView.as_view(url="/admin"), name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(
        template_name='employee_information/login.html', redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    path('about', views.about, name="about-page"),
    path('departments', views.departments, name="department-page"),
    path('manage_departments', views.manage_departments,
         name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions,
         name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
    path('employees', views.employees, name="employee-page"),
    path('manage_employees', views.manage_employees,
         name="manage_employees-page"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('view_employee', views.view_employee, name="view-employee-page"),
    path('checking_salary', views.checking_salary, name="checking-page"),
    path('visualization', views.visualization, name="visualization-page"),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('delete_employee/', views.delete_employee, name='delete_employee'),
    path('result', views.result, name='result'),

]
